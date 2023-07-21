# Define all the transformations used for data augmentation
import torch
from torchvision import transforms
import numpy as np

imagenetnorm = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
def parse_transforms(transforms_str, image_size):
    """
    Define the transformations to be applied to the images
    """
    transforms_list = []
    for transform in transforms_str:
        if 'imagenetnorm' in transform.lower() and 'miniimagenetnorm' not in transform.lower():
            transforms_list.append(imagenetnorm)
        elif 'resize' in transform.lower() and 'random' not in transform.lower():
            if '_' in transform:
                ratio = transform.split('_')[-1]
                if '/' in transform:
                    ratio = eval(ratio)
                else:
                    ratio = float(ratio)
            else:
                ratio = 1
            transforms_list.append(transforms.Resize(int(image_size*ratio)))
        elif 'randomresizedcrop' in transform.lower():
            transforms_list.append(transforms.RandomResizedCrop(image_size))
        elif 'centercrop' in transform.lower():
            transforms_list.append(transforms.CenterCrop(image_size))
        elif 'randomhorizontalflip' in transform.lower():
            if '_' in transform:
                p = float(transform.split('_')[-1])
            else:
                p = 0.5
            transforms_list.append(transforms.RandomHorizontalFlip(p=p))
        elif 'randomverticalflip' in transform.lower():
            if '_' in transform:
                p = float(transform.split('_')[-1])
            else:
                p = 0.5
            transforms_list.append(transforms.RandomVerticalFlip(p=p))
        elif 'colorjitter' in transform.lower():
            if '_' in transform:
                brightness = transform.split('_')[1:]
                if len(brightness) == 1:
                    brightness = float(brightness[0])
                    contrast, saturation = brightness, brightness
                else:
                    brightness, contrast, saturation = float(brightness[0]), float(brightness[1]), float(brightness[2])
            else:
                brightness, contrast, saturation = 0.4, 0.4, 0.4
            transforms_list.append(transforms.ColorJitter(brightness=brightness, contrast=contrast, saturation=saturation))     
        elif 'clip' in transform.lower():
            import clip
            clip_name = {"clip_b32":'ViT-B/32',"clip_b16":'ViT-B/16',"clip_l14":'ViT-L/14',"clip_l16_336px":'ViT-L/14@336px'}[transform.lower()]
            transforms_list.append(clip.load(clip_name, device='cpu')[1])
        else:
            raise ValueError('Unknown transformation: {}'.format(transform))
    return transforms.Compose(transforms_list)