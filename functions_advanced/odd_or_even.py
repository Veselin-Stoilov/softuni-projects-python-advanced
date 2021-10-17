command = input()
numbers = [int(x) for x in input().split()]

if command == 'Odd':
    num_sum = sum([x for x in numbers if x % 2 != 0])
else:
    num_sum = sum([x for x in numbers if x % 2 == 0])

print(num_sum * len(numbers))