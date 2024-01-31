import os
import pandas as pd
from collections import Counter
def process_file(file_path, word_freq):
        if file_path.lower().endswith(('.xlsx', '.txt')):
            if file_path.lower().endswith('.xlsx'):
                df = pd.read_excel(file_path)
                text = ' '.join(map(str, df.values.flatten()))
            else:
                with open(file_path, 'r') as txt_file:
                    text = txt_file.read()

            word_freq.update(text.split())
def list_files(target_directory):
    file_paths = []
    word_freq = Counter()

    for root, dirs, files in os.walk(target_directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
            process_file(file_path, word_freq)

    print("\n".join(["List of file paths:"] + file_paths))
    print("\nWord frequency for .xlsx and .txt files:")
    print("\n".join([f"{word}: {frequency}" for word, frequency in word_freq.items()]))

target_directory = input("Enter the target directory path: ")

if os.path.exists(target_directory) and os.path.isdir(target_directory):
    list_files(target_directory)
else:
    print("Invalid directory path. Please provide a valid directory.")



