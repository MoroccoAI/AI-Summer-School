#### script for running the training
import torch
import argparse
from models import prepareBackbone, prepareClassifier
from augmentations import parse_transforms
from PIL import Image
import random
import numpy as np
import os
import math
from tqdm import tqdm
from collections import Counter
import warnings 
warnings.filterwarnings("ignore")

def get_optimizer(name, model, lr, wd, momentum):
    if name.lower() == 'adam':
        return torch.optim.Adam(model.parameters(), lr=lr, weight_decay=wd)
    elif name.lower() == 'adamw':
        return torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=wd)
    elif name.lower() == 'sgd':
        return torch.optim.SGD(model.parameters(), lr=lr, momentum=momentum, weight_decay=wd)
def get_scheduler(name, optimizer, max_n_steps, lr, end_lr):
    if len(name) == 0 or name == "" or name == '': 
        return None
    if name.lower() == 'cosine':
        return torch.optim.lr_scheduler.CosineAnnealingLR(optimizer=optimizer, T_max=max_n_steps, eta_min=lr*end_lr)
    elif name.lower() == 'linear':
        return torch.optim.lr_scheduler.LinearLR(optimizer=optimizer, end_lr=end_lr, max_steps=max_n_steps)
    else:
        return None
    
def get_args():
    parser = argparse.ArgumentParser()
    # training parameters
    parser.add_argument("--lr", type=float, default=-1, help="learning rate")
    parser.add_argument("--end-lr-factor", type=float, default=0, help="ending learning rate factor end_lr=lr*end_lr_factor")
    parser.add_argument("--wd", type=float, default=-1, help="weight decay")
    parser.add_argument("--mmt", type=float, default=0.9, help="momentum")
    parser.add_argument("--optimizer", type=str, default='sgd', help="optimizer")
    parser.add_argument("--scheduler", type=str, default='constant', help="optimizer")
    parser.add_argument("--batch-size", type=int, default=128, help="batch size")
    parser.add_argument('--device', type=str, default='cpu')
    parser.add_argument("--backbone", type=str, default='clip_v32', help="classifier used to train on the embeddings")
    parser.add_argument("--epochs", type=int, default=20, help="total number of training epochs")
    parser.add_argument("--classifier", type=str, default="ncm", help="classifier to use, options are: logit or ncm")
    parser.add_argument("--n-aug", type=int, default=1, help="if classifier is ncm, number of augmentations to apply")
    parser.add_argument("--n-shots", type=int, default=6, help="number of training images per class")
    parser.add_argument("--val-shots", type=int, default=0, help="number of training images per class")
    
    parser.add_argument("--dropout", type=float, default=0.1, help="dropout")
    parser.add_argument("--preprocessing", type=str, default="ME", help="transforms")
    parser.add_argument("--seed", type=int, default=-1, help="seed")
    parser.add_argument("--image-size", type=int, default=224, help="seed")
    parser.add_argument("--dataset-path", type=str, default="", help="dataset path")
    parser.add_argument("--train-transforms", type=str, default="", help="transforms")
    parser.add_argument("--val-transforms", type=str, default="", help="transforms")
    parser.add_argument("--test-transforms", type=str, default="", help="transforms")
    parser.add_argument("--test-dataset-path", type=str, default="", help="different test dataset than training")
    # logging and saving parameters
    parser.add_argument("--debug", action="store_true", help="debug mode")
    parser.add_argument("--imbalanced", action="store_true", help="don't balance the dataset")
    parser.add_argument("--save-model", type=str, default="", help="save model")
    parser.add_argument("--wandb", type=str, default="", help="use wandb")
    parser.add_argument("--wandbProjectName", type=str, default="BeRadar", help="wandb project name")
    parser.add_argument("--log-metrics", type=str, default="", help="wandb project name")

    args = parser.parse_args()
    if args.wandb == '""' or args.wandb == "''":
        args.wandb = ''
    if args.lr < 0:
        defaut_values_lr = {'sgd':0.1, 'adamw':1e-3, 'adam':1e-3, 'adagrad':0.1, 'adadelta':1e-3, 'rmsprop':1e-3}
        args.lr = defaut_values_lr[args.optimizer.lower()]
    if args.wd < 0:
        default_values_wd = {'sgd':5e-4, 'adamw':1e-2, 'adam':0, 'adagrad':0, 'adadelta':0, 'rmsprop':0}
        args.wd = default_values_wd[args.optimizer.lower()]
    if args.seed < 0:
        args.seed = random.randint(0, 1000000)
    args.save_model = '' if args.save_model == '""' else args.save_model
    try: 
        args.train_transforms = eval(args.train_transforms)
    except: 
        args.train_transforms = [args.train_transforms]
    try:           
        args.test_transforms = eval(args.test_transforms)
    except: 
        args.test_transforms = [args.test_transforms]
    
    # fix seed to reproduce results
    random.seed(args.seed)
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    torch.cuda.manual_seed(args.seed)
    print(f'Args: {args}')
    return args
class Dataset():
    """
    Return a dataset with class-level features
    """
    def __init__(self, data, targets, path, transforms):
        self.data = data
        self.targets = targets
        self.path = path
        self.transforms = transforms
    def __getitem__(self, idx):
        """
        """
        target = self.targets[idx]
        etl = Image.open(os.path.join(self.path, self.data[idx])).convert('RGB')
        etl = self.transforms(etl)
        return etl, target, idx
    def __len__(self):
        return len(self.data)

def train(classifier, backbone, train_loader, val_loader, args): 
    with torch.no_grad():
        features, labels = [], []
        for n_aug in range(args.n_aug): 
            print(f'n_aug:{n_aug}', end='\r')
            train_iter = enumerate(train_loader)
            for _, (data, targets, _) in train_iter: 
                data = data.to(args.device)
                feats = backbone(data)
                features.append(feats.to('cpu'))
                labels.append(targets)
        features = torch.cat(features)
        labels = torch.cat(labels)
    if args.classifier == 'ncm': # no need for training, just save the nearest class mean features
        # get all feature shots 
        classifier.cache_shots(features, labels)

    elif args.classifier == 'logit': # then u need to train 
        criterion = torch.nn.CrossEntropyLoss()
        optimizer = get_optimizer(args.optimizer, net, args.lr, args.wd, args.mmt)
        scheduler = get_scheduler(args.scheduler, optimizer, args.epochs, args.lr, args.end_lr_factor)
    return classifier

def test(classifier, backbone, loader, args): 
    classifier.eval()
    backbone.eval()
    with torch.no_grad(): # stop gradient updating
        tp, fp, fn, tn, total_count = 0., 0., 0., 0., 0.
        for idx, (data, targets, indices) in enumerate(loader): 
            data = data.to(args.device)
            targets = targets.to(args.device)
            features = backbone(data)
            predictions = classifier(features)
            probas, winners = predictions.max(dim=1)
            tp += (winners[targets==1]==1).sum().cpu()
            fp += (winners[targets==0]==1).sum().cpu()
            fn += (winners[targets==1]==0).sum().cpu()
            tn += (winners[targets==0]==0).sum().cpu()
            total_count += len(targets)

            # get indices of false positives: 
    accuracy = (tp+tn)/total_count
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    return accuracy, precision, recall
def balance_dataset(data, targets, test_targets, test_idx, args):
    occurences = list(Counter(np.array(test_targets)).values())
    if min(occurences)!= max(occurences) and not args.imbalanced:
        min_num_elements = min(occurences)
        print(f'Test set is imbalanced, balancing it to {min_num_elements} per class')
        new_test_idx = test_idx[test_targets==0][:min_num_elements].tolist() + test_idx[test_targets==1][:min_num_elements].tolist()
        test_idx = torch.tensor(new_test_idx)
        test_targets = targets[test_idx]
        print(f'New test set size: {Counter(np.array(test_targets))}')
        data_test = [data[idx] for idx in test_idx]
    return data_test, test_idx, test_targets
def main(args):
    # train_transforms = parse_transforms(args.train_transforms, args.image_size)
    # test_transforms = parse_transforms(args.test_transforms, args.image_size)
    # ### load path for dataset
    # data, class_count, targets, class_names = [], 0, [], []
    # for folder in os.listdir(args.dataset_path)[:]:
    #     data_class = list(map(lambda x: os.path.join(folder, x),os.listdir(os.path.join(args.dataset_path, folder))))[:]
    #     data += data_class
    #     targets += [class_count]*len(data_class)
    #     class_names.append(folder)
    #     class_count +=1 
    # indices = torch.randperm(len(targets)) # randomly permuting data
    # targets = torch.tensor(targets)

    # if args.test_dataset_path == "":
    #     positives_indices = indices[targets==1]
    #     negative_indices = indices[targets==0]
    
    #     train_idx = torch.cat([positives_indices[:args.n_shots], negative_indices[:args.n_shots]])
    #     val_idx = torch.cat([positives_indices[args.n_shots:args.n_shots+args.val_shots], negative_indices[args.n_shots:args.n_shots+args.val_shots]])
    #     test_size = min(len(positives_indices), len(negative_indices))-args.n_shots-args.val_shots
    #     test_idx = torch.cat([positives_indices[args.n_shots+args.val_shots:args.n_shots+args.val_shots+test_size], negative_indices[args.n_shots+args.val_shots:args.n_shots+args.val_shots+test_size]])

    #     data_train = [data[idx] for idx in train_idx]
    #     data_val   = [data[idx] for idx in val_idx]
    #     data_test  = [data[idx] for idx in test_idx]
    #     train_targets = targets[train_idx]
    #     val_targets = targets[val_idx]
    #     test_targets = targets[test_idx]
    # else: 
    #     # get test set separately
    #     split = [1, 0] 
    #     split = [math.floor(len(indices)*split[0]), math.floor(len(indices)*(split[0]+split[1]))]
    #     data_test, class_count, test_targets = [], 0, []
    #     for folder in os.listdir(args.test_dataset_path)[:]:
    #         data_class = list(map(lambda x: os.path.join(folder, x),os.listdir(os.path.join(args.test_dataset_path, folder))))[:]
    #         data_test += data_class
    #         test_targets += [class_count]*len(data_class)
    #         class_count +=1 
    #     test_targets = torch.tensor(test_targets)
    #     test_idx = torch.arange(len(test_targets))
    # # check if test set is imbalanced then balance them 
    # # data_test, test_idx, test_targets = balance_dataset(data, targets, test_targets, test_idx, args)

    # num_classes = len(torch.unique(train_targets))
    # print(f'{num_classes} classes, len(train)={len(data_train)}, len(val)={len(data_val)}, len(test)={len(data_test)}')
    # print(f'Class names={class_names}')

    # # Create datasets
    # train_dataset = Dataset(data_train, train_targets, args.dataset_path, train_transforms)
    # val_dataset = Dataset(data_val, val_targets, args.dataset_path, test_transforms) if len(val_idx)>0 else []
    # test_dataset = Dataset(data_test, test_targets, args.dataset_path, test_transforms)

    # # Create DataLoaders
    # train_loader = torch.utils.data.DataLoader(train_dataset, batch_size = args.batch_size, shuffle = False, num_workers = min(os.cpu_count(), 8))
    # val_loader = torch.utils.data.DataLoader(val_dataset, batch_size = args.batch_size, shuffle = False, num_workers = min(os.cpu_count(), 8))
    # test_loader = torch.utils.data.DataLoader(test_dataset, batch_size = args.batch_size, shuffle = False, num_workers = min(os.cpu_count(), 8))

    # backbone, num_features = prepareBackbone(args.backbone, args.device) # load network
    # backbone = backbone.to(args.device)
    # classifier = prepareClassifier(args.classifier, num_features, num_classes, 'cpu', args) # load classifier, send to cpu to avoid memory issues

    # # train classifier
    # classifier = train(classifier, backbone, train_loader, val_loader, args) 
    # # test model
    # val_accuracy, val_precision, val_recall = test(classifier, backbone, val_loader, args) if args.val_shots>0 else 0, 0, 0
    # accuracy, precision, recall = test(classifier, backbone, test_loader, args)
    # train_size, val_size, test_size  = len(data_train), len(data_val), len(data_test)
    # return accuracy, precision, recall, val_accuracy, val_precision, val_recall, train_size, val_size, test_size
    pass
if __name__=="__main__":
    args = get_args()
    train_transforms = parse_transforms(args.train_transforms, args.image_size)
    test_transforms = parse_transforms(args.test_transforms, args.image_size)
    ### load path for dataset
    data, class_count, targets, class_names = [], 0, [], []
    for folder in os.listdir(args.dataset_path)[:]:
        data_class = list(map(lambda x: os.path.join(folder, x),os.listdir(os.path.join(args.dataset_path, folder))))[:]
        data += data_class
        targets += [class_count]*len(data_class)
        class_names.append(folder)
        class_count +=1 
    indices = torch.randperm(len(targets)) # randomly permuting data
    targets = torch.tensor(targets)

    if args.test_dataset_path == "":
        positives_indices = indices[targets==1]
        negative_indices = indices[targets==0]
    
        train_idx = torch.cat([positives_indices[:args.n_shots], negative_indices[:args.n_shots]])
        val_idx = torch.cat([positives_indices[args.n_shots:args.n_shots+args.val_shots], negative_indices[args.n_shots:args.n_shots+args.val_shots]])
        test_size = min(len(positives_indices), len(negative_indices))-args.n_shots-args.val_shots
        test_idx = torch.cat([positives_indices[args.n_shots+args.val_shots:args.n_shots+args.val_shots+test_size], negative_indices[args.n_shots+args.val_shots:args.n_shots+args.val_shots+test_size]])

        data_train = [data[idx] for idx in train_idx]
        data_val   = [data[idx] for idx in val_idx]
        data_test  = [data[idx] for idx in test_idx]
        train_targets = targets[train_idx]
        val_targets = targets[val_idx]
        test_targets = targets[test_idx]
    else: 
        positives_indices = indices[targets==1]
        negative_indices = indices[targets==0]
        train_size = min(args.n_shots, min(len(positives_indices), len(negative_indices)))
        train_idx = torch.cat([positives_indices[:train_size], negative_indices[:train_size]])
        data_train = [data[idx] for idx in train_idx]
        train_targets = targets[train_idx]
        val_idx, val_targets, data_val = [], [], []
        
        data_test, class_count, test_targets = [], 0, []
        for folder in os.listdir(args.test_dataset_path)[:]:
            data_class = list(map(lambda x: os.path.join(folder, x),os.listdir(os.path.join(args.test_dataset_path, folder))))[:]
            data_test += data_class
            test_targets += [class_count]*len(data_class)
            class_count +=1 
        test_targets = torch.tensor(test_targets)
        test_idx = torch.arange(len(test_targets))
        # balance them 
        positives_indices = test_idx[test_targets==1]
        negative_indices = test_idx[test_targets==0]
        test_size = min(len(positives_indices), len(negative_indices))
        test_idx = torch.cat([positives_indices[:test_size], negative_indices[:test_size]])
        test_targets = test_targets[test_idx]
        data_test = [data_test[idx] for idx in test_idx]

    num_classes = len(torch.unique(train_targets))
    print(f'{num_classes} classes, len(train)={len(data_train)}, len(val)={len(data_val)}, len(test)={len(data_test)}')
    print(f'Class names={class_names}')

    # Create datasets
    train_dataset = Dataset(data_train, train_targets, args.dataset_path, train_transforms)
    val_dataset = Dataset(data_val, val_targets, args.dataset_path, test_transforms) if len(val_idx)>0 else []
    test_dataset = Dataset(data_test, test_targets, args.test_dataset_path, test_transforms)

    # Create DataLoaders
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size = args.batch_size, shuffle = False, num_workers = min(os.cpu_count(), 8))
    val_loader = torch.utils.data.DataLoader(val_dataset, batch_size = args.batch_size, shuffle = False, num_workers = min(os.cpu_count(), 8))
    test_loader = torch.utils.data.DataLoader(test_dataset, batch_size = args.batch_size, shuffle = False, num_workers = min(os.cpu_count(), 8))

    backbone, num_features = prepareBackbone(args.backbone, args.device) # load network
    backbone = backbone.to(args.device)
    classifier = prepareClassifier(args.classifier, num_features, num_classes, 'cpu', args) # load classifier, send to cpu to avoid memory issues

    # train classifier
    classifier = train(classifier, backbone, train_loader, val_loader, args) 
    # test model
    if args.val_shots>0:
        val_accuracy, val_precision, val_recall = test(classifier, backbone, val_loader, args) 
    else: 
        val_accuracy, val_precision, val_recall = 0, 0, 0
    accuracy, precision, recall = test(classifier, backbone, test_loader, args)
    train_size, val_size, test_size  = len(data_train), len(data_val), len(data_test)
    # accuracy, precision, recall, val_accuracy, val_precision, val_recall, train_size, val_size, test_size = main(args)
    print(f'Seed:{args.seed}, Accuracy: {100*accuracy:.2f}%, Precision: {100*precision:.2f}%, Recall: {100*recall:.2f}%')
    if args.log_metrics:
        if not os.path.exists(args.log_metrics):
            os.makedirs(args.log_metrics)
        name = 'logs_cross_domain.txt' if args.test_dataset_path != '' else 'logs.txt'
        with open(os.path.join(args.log_metrics, name), 'a') as f:
            f.write(f'Seed:{args.seed}, n_shots:{args.n_shots}, backbone={args.backbone}, n_aug={args.n_aug}, len_train={train_size}, len_val={val_size}, len_test={test_size}, Val: [Accuracy: {100*val_accuracy}, Precision: {100*val_precision}, Recall: {100*val_recall}], Test: [Accuracy: {100*accuracy}, Precision: {100*precision}, Recall: {100*recall}]\n')
    