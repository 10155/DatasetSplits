from dataset_info import dataset_info
import torch 
import os

def load_split_datasets(folder_to_be_loaded_from, file_name):

    count = 0
    for filename in os.listdir(folder_to_be_loaded_from):
        if file_name in filename:
            count += 1

    for i in range(count):

        path = f'{folder_to_be_loaded_from}/{file_name}_{i+1}.pth'
        print(f'loaded from {path}')
        training= torch.load(f'{path}')

        dataset_info(training)
