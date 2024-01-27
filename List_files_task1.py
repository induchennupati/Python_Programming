import os
import pandas as pd
from collections import Counter

def list_files_and_word_frequency(target_directory):
    file_paths = []
    word_frequency = Counter()

    for root, _, files in os.walk(target_directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)

            if file_path.lower().endswith(('.xlsx', '.txt')):
               
                if file_path.lower().endswith('.xlsx'):
                    try:
                        df = pd.read_excel(file_path)
                        text = ' '.join(map(str, df.values.flatten()))
                    except pd.errors.EmptyDataError:
                        text = ''
                else:
                    try:
                        with open(file_path, 'r', encoding='utf-8') as txt_file:
                            text = txt_file.read()
                    except UnicodeDecodeError:
                        print(f"Failed to decode file '{file_path}' with encoding 'utf-8'.")

                words = text.split()
                word_frequency.update(words)

    print("List of file paths:")
    for path in file_paths:
        print(path)

    print("\nWord frequency for .xlsx and .txt files:")
    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")

target_directory = input("Enter the target directory path: ")

if os.path.exists(target_directory) and os.path.isdir(target_directory):
    list_files_and_word_frequency(target_directory)
else:
    print("Invalid directory path. Please provide a valid directory.")

