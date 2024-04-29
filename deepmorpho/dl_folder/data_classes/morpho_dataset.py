import os
import torch
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import timm
import json


class EmbryoDataset(Dataset):
    def __init__(self, annotations, images, transform=None):
        self.annotations = annotations
        self.images = images
        self.labels = self.get_labels()
        self.transform = transform


    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, idx):
        label = self.annotations[idx][1]
        image = self.images[idx][1]
        if image.mode != 'RGB':
            image = image.convert('RGB')



        if self.transform:
            image = self.transform(image)

        return image, label


    def get_labels(self):
        labels = []
        for annotation in self.annotations:
            labels.append(annotation[1])
        return labels

