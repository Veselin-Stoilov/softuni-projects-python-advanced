file_name = r'text_documents\text.txt'

try:
    open(file_name, 'r')
    print('File found')
except:
    print('File not found')