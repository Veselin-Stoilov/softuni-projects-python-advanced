import os

file_path = "text_documents/my_first_file.txt"

try:
    os.remove(file_path)
except:
    print('File already deleted!')