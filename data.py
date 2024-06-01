import pandas as pd
import os

def load_data(file_path):
    # Load data from Excel file and skip the first row
    data = pd.read_excel(file_path, header=1).to_dict()
    return data

def scan_image(idx=1):
    paths = os.listdir('./药材图片')
    path = os.path.join('./药材图片', paths[0])
    paths = os.listdir(path)
    numbers = []
    for p in paths:
        ss = ''
        for c in p:
            if c in '0123456789':
                ss += c
            else:
                break
        numbers.append(ss)
    index = numbers.index(str(idx))
    path = os.path.join(path, paths[index])
    return path

def fetch_image(idx=1):
    path = scan_image(idx)
    images = os.listdir(path)
    return [os.path.abspath(os.path.join(path, image)) for image in images]

data = load_data('./药材300种.xlsx')

length = len(data[list(data.keys())[0]])

if __name__ == '__main__':
    print(data.keys())
    print(length)
    print(fetch_image(2))
