file_path = r'text_documents\my_first_file.txt'

content = 'I just created my first file'

with open(file_path, 'w') as file:
    file.write(content)