from math import log

num = int(input())
base = input()
if base == 'natural':
    result = log(num)
else:
    result = log(num, int(base))


print(f'{result:.2f}')