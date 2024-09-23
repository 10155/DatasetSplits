from torchvision.datasets import MNIST, CIFAR100
import os
from dataset_info import dataset_info
from bound_split import bound_split
from save_split_datasets import save_split_datasets
from load_split_datasets import load_split_datasets
from file_naming import file_naming

# Take in your data

#test_dataset = MNIST('./data', train=False, download=True)
#train_dataset = MNIST('./data', train=True, download=True)

train_dataset = CIFAR100('./data', train=True, download=True)
test_dataset = CIFAR100('./data', train=False, download=True)

# nothing below here should need to be changed

# info about the data

dataset_info(test_dataset)
dataset_info(train_dataset)

def feed_in_dataset(dataset, folder):

    directory = f"./data/split/{folder}"

    if not os.path.exists(directory):
        os.makedirs(directory)

    file_name = file_naming(dataset)

    list_of_split_datasets = bound_split(dataset,split_into=5)

    save_split_datasets(list_of_split_datasets, directory, file_name)

    load_split_datasets(directory, file_name)

# The magic starts here

# This should be a name such as MNIST or CIFAR-100
folder = f"{train_dataset.__class__.__name__}" 

feed_in_dataset(test_dataset, folder)

feed_in_dataset(train_dataset, folder)