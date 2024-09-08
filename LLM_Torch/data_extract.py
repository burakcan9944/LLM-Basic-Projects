import lzma
import os
from tqdm import tqdm
"""Download the data from dataset_find.txt, make a folder with all of them and then run it with this code"""
"""Verileri dataset_find.txt dosyasından indirin, hepsini içeren bir klasör oluşturun ve ardından şu kodla çalıştırın"""
def xz_files_in_dir(directory):
    files = []
    for filename in os.listdir(directory):
        if filename.endswith(".xz") and os.path.isfile(os.path.join(directory, filename)):
            files.append(filename)

    return files

folder_path = "/openwebtext"
output_path_train = "output_train.txt"
output_path_val = "output_valid.txt"
vocab_file = "vocab.txt"


files = xz_files_in_dir(folder_path)

total_files = len(files)

split_index = int(total_files * 0.9) #%90 train %10 valid
files_train = files[:split_index]
files_val = files[split_index:]

vocab = set()

#train
with open(output_path_train, "w", encoding="utf-8") as outfile:
    for filename in tqdm(files_train, total=len(files_train)):
        file_path = os.path.join(folder_path, filename)
        with lzma.open(file_path, "rt", encoding="utf-8") as infile:
            text = infile.read()
            outfile.write(text)
            characters = set(text)
            vocab.update(characters)

#valid
with open(output_path_val, "w", encoding="utf-8") as outfile:
    for filename in tqdm(files_val, total=len(files_val)):
        file_path = os.path.join(folder_path, filename)
        with lzma.open(file_path, "rt", encoding="utf-8") as infile:
            text = infile.read()
            outfile.write(text)
            characters = set(text)
            vocab.update(characters)

with open(vocab_file, "w", encoding="utf-8") as vfile:
    for char in vocab:
        vfile.write(char + "\n")
