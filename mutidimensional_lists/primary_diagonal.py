def matrix_creator():
    matrix = []
    for _ in range(n):
        matrix.append([int(x) for x in input().split()])
    return matrix


n = int(input())

matrix = matrix_creator()
diagonal = []

for i in range(n):
    diagonal.append(matrix[i][i])

print(sum(diagonal))