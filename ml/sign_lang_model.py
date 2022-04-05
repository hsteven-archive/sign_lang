import torch
import torch.nn as nn
import torch.nn.functional as F
import cv2
import numpy as np

class SignLangModel(nn.Module):
    def __init__(self):	
        super(SignLangModel, self).__init__()
    
        self.conv1 = nn.Sequential(
        nn.Conv2d(1,80,kernel_size=5),
        nn.BatchNorm2d(80),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2,stride=2)
        )
    
        self.conv2 = nn.Sequential(     
        nn.Conv2d(80,80,kernel_size=5),
        nn.BatchNorm2d(80),
        nn.ReLU(),
        nn.MaxPool2d(kernel_size=2,stride=2)
        )

        self.fc1 = nn.Sequential(
        nn.Linear(1280, 250),
        nn.ReLU()
        )

        self.fc2 = nn.Sequential(
        nn.Linear(250, 25),
        nn.LogSoftmax(dim=1)
        )


    def forward(self,x):
        x = self.conv2(self.conv1(x))
        x = x.view(x.size(0), -1)
        x = self.fc2(self.fc1)

        return x