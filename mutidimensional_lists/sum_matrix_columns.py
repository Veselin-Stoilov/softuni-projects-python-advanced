def matrix_creator():
    matrix = []
    for _ in range(n):
        matrix.append([int(x) for x in input().split()])
    return matrix


n, m = (int(x) for x in input().split(', '))

matrix = matrix_creator()
sum_columns = []

for column in range(m):
    current_sum = 0
    for row in range(n):
        current_sum += matrix[row][column]
    sum_columns.append(current_sum)

for el in sum_columns:
    print(el)