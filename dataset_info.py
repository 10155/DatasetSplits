import numpy as np
from collections import Counter

def dataset_info(dataset):

    
    images = []
    labels = []
    for img, label in dataset:
        images.append(np.asarray(img))
        labels.append(label)

    # Convert lists to NumPy arrays
    images = np.array(images)
    labels = np.array(labels)

    # Print shapes to verify
    print(f'\nImages shape: {images.shape}')
    print(f'Labels shape: {labels.shape}')

    class_counts = Counter(list(labels))

    for lab in np.unique(labels):
        print(f"Class {lab}: {class_counts[lab]} samples")