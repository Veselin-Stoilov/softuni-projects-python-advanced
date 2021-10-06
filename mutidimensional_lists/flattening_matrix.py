rows = int(input())
matrix = []
for _ in range(rows):
    matrix += [int(x) for x in input().split(', ')]
print(matrix)