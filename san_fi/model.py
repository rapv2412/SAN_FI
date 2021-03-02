import torch
import torch.nn as nn 
import torch.utils.data import Dataset, Dataloader

# Just following the paper

class basicSAN(nn.Module):
    def __init__(self,input_size,num_heads,num_hidden,dropout):
        super().__init__()      # Inherit super class from nn.module

        self.input_size = input_size
        self.num_heads = num_heads
        self.num_hidden = num_hidden
        self.device = device

        self.fc1 = nn.Linear(input_size,input_size) 
        self.softmax = nn.Softmax(dim=1) # Per row
        self.activation = nn.SELU()
        self.sigmoid = nn.sigmoid()
        self.dropout = nn.Dropout(p = dropout)
        self.fc2 = nn.Linear(num_heads,num_hidden)
        self.fc3 = 

    def forward(self,x):
        x = self.fc1(x)
        x = self.softmax(x)
        x 

#if __name__ == '__main__':     # So we can run the script (sometimes)