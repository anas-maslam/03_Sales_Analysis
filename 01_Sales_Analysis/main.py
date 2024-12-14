import os
import numpy as np


def read_dataset(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split(','))
    return data


if __name__ == "__main__":
    dataset_path = ""
    dataset = read_dataset(dataset_path)
    
