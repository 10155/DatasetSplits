from dataset_info import dataset_info
import torch 

def save_split_datasets(datasets, folder_to_save_to, file_name):

    int = 1

    for split_dataset in datasets:
        dataset_info(split_dataset)

        path = f"{folder_to_save_to}/{file_name}_{int}.pth"
        print(f'saved as {path} \n')
        torch.save(split_dataset, path)
        int = int + 1