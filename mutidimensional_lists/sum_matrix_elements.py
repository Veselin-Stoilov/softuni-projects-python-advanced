n, m = [int(x) for x in input().split(', ')]

matrix = []
matrix_sum = 0

for r in range(n):
    column = [int(x) for x in input().split(', ')]
    matrix.append(column)
    matrix_sum += sum(column)

print(matrix_sum)

print(matrix)