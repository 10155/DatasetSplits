from torch.utils.data import Subset

def bound_split(dataset, split_into):

    num_classes = len(dataset.classes)
    intervals_size = int(num_classes / split_into)

    array = list(range(num_classes))
    intervals = [array[i:i + intervals_size] for i in range(0, num_classes, intervals_size)]

    print(f'\nThe dataset has {num_classes} classes and will be split into {split_into} intervals')
    print(f'Theses intervals will be {intervals}')

    sub_datasets = []
    for interval in intervals:
        
        subset_indices = [i for i, (_, label) in enumerate(dataset) if label in interval]

        sub_datasets.append(Subset(dataset, subset_indices))

    return sub_datasets