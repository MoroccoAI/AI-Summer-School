import torch 
import torch.nn as nn
import torch.nn.functional as F
import numpy as np 
import clip

class LogitHead(nn.Module):
    def __init__(self, in_features, num_classes, args, bias=False, logit_scale=float(np.log(1 / 0.07))):
        super().__init__()
        self.head = nn.Linear(in_features, num_classes, bias=bias)
        self.logit_scale = logit_scale
        self.logit_scale = torch.FloatTensor([logit_scale]).cuda()

    def forward(self, x):
        x = F.normalize(x, dim=1)
        x = self.head(x)
        x = x * self.logit_scale.exp()
        return x

class NCM(nn.Module):
    def __init__(self, in_features, num_classes, args, device="cuda:0"):
        super().__init__()
        self.device = device
        self.preprocessing = args.preprocessing
    def cache_shots(self, shots, labels):
        self.centroids = []
        shots = shots.to(self.device)
        self.labels = labels
        self.mean = shots.mean(dim=0)
        if self.preprocessing:
            for processing in self.preprocessing:
                if processing == "M":
                    shots = shots - self.mean
                elif processing == "E":
                    shots = shots / shots.norm(dim=1, keepdim=True)
        for label in torch.unique(labels):
            self.centroids.append(torch.mean(shots[labels==label], dim=0))
        self.centroids = torch.stack(self.centroids, dim=0)
    def forward(self, features):
        # make classification 
        features = features.to(self.device)
        if self.preprocessing:
            for processing in self.preprocessing:
                if processing == "M":
                    features = features - self.mean
                elif processing == "E":
                    features = features / features.norm(dim=1, keepdim=True)
        distances = torch.norm(features.unsqueeze(1) - self.centroids.unsqueeze(0), dim=2)
        return -distances

class Clip(nn.Module):
    def __init__(self, name, device):
        super(Clip, self).__init__()
        self.backbone = clip.load(name, device=device)[0]
    def forward(self, x):
        out = self.backbone.encode_image(x)
        return out
def prepareBackbone(backbone, device):
    return {
        "clip_b32": lambda: (Clip('ViT-B/32', device), 512),
        "clip_b16": lambda: (Clip('ViT-B/16', device), 512),
        "clip_l14": lambda: (Clip('ViT-L/14', device), 768),
        "clip_l16_336px": lambda: (Clip('ViT-L/14@336px', device), 768)
        }[backbone.lower()]()

def prepareClassifier(classifier, in_features, num_classes, device, args):
    return {
        "logit": LogitHead, 
        "ncm": NCM
    }[classifier.lower()](in_features, num_classes, args).to(device)