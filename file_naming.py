def file_naming(dataset):

    dataset_name = dataset.__class__.__name__

    if hasattr(dataset, 'train'):
        if dataset.train:
            dataset_type = 'train'
        else:
            dataset_type = 'test'
    else:
        dataset_type = 'unknown'

    return f'{dataset_name}_{dataset_type}'