file_name = r'text_documents\numbers.txt'

file = open(file_name, 'r')

num_sum = 0

numbers = [int(x) for x in file.read() if x.isdigit()]

for num in numbers:
    num_sum += int(num)

print(num_sum)
