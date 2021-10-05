rows = int(input())

matrix = []

for r in range(rows):
    matrix.append([int(x) for x in input().split(', ') if int(x) % 2 == 0])
print(matrix)