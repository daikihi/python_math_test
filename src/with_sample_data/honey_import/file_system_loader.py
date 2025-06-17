# this file managing read data from file system
import os
import pandas as pd

def get_file_list(directory):
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist.")
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"The path {directory} is not a directory.")
    
    file_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    print(file_list)
    return file_list


def load_xls_binary_data_from_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    xls_file_root = pd.read_excel(file_path)
    return xls_file_root