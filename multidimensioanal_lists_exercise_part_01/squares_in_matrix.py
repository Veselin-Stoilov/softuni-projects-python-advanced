def matrix_creator():
    matrix = []
    for _ in range(n):
        matrix.append(input().split())
    return matrix


n, m = (int(x) for x in input().split())
matrix = matrix_creator()
pattern_counter = 0

for r in range(n - 1):
    for c in range(m - 1):
        if matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
            pattern_counter += 1
print(pattern_counter)

