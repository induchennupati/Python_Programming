import os
from threading import Thread

def encryptTextFile(filepath, encrypt_value):
    data = ''
    encrypted_data = ''

    # Check if the file exists before attempting to read it
    if os.path.exists(filepath):
        with open(filepath, 'r') as file:
            data = file.read()

    for char in data:
        ascii_value = ord(char)
        if 65 <= ascii_value <= 90:
            encrypted_data = encrypted_data + chr((ascii_value + encrypt_value - 65) % 26 + 65)
        else:
            encrypted_data = encrypted_data + char
            
    # Create the new file path by appending 'encrypted' to the original file path
    new_filepath = filepath + 'encrypted'
    
    # Write the encrypted data to the new file
    with open(new_filepath, 'w') as file:
        file.write(encrypted_data)

# User input for the target directory and encrypt value
path = input('Input:')
encrypt_value = int(input('Enter the encrypt value:'))

# List to store file paths of .txt files
file_paths = []

# Collect file paths for .txt files in the target directory
for dirpath, dirnames, filenames in os.walk(path):
    for x in filenames:
        filepath = os.path.join(dirpath, x)
        print(filepath)  # Print the original file path
        if filepath.lower().endswith('.txt'):
            file_paths.append(filepath)

# List to keep track of Thread objects
threads = []

# Create a new thread for each .txt file
for filepath in file_paths:
    t1 = Thread(target=encryptTextFile, args=(filepath, encrypt_value,))
    t1.start()
    threads.append(t1)

# Wait for all threads to finish before proceeding
for thread in threads:
    thread.join()


