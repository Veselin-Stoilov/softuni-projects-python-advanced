def matrix_creator():
    matrix = []
    for _ in range(n):
        matrix.append([int(x) for x in input().split()])
    return matrix


n = int(input())

matrix = matrix_creator()
primary_diagonal = []
secondary_diagonal = []

for r in range(n):
    primary_diagonal.append(matrix[r][r])
    secondary_diagonal.append(matrix[r][n - r - 1])

diagonal_difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(diagonal_difference)
