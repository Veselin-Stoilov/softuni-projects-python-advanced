def matrix_creator():
    matrix = []
    for _ in range(n):
        matrix.append([int(x) for x in input().split()])
    return matrix


n, m = (int(x) for x in input().split())
matrix = matrix_creator()
max_sum = 0
current_sub_matrix = []
max_sub_matrix = []

for r in range(n - 2):
    for c in range(m - 2):

        current_sum = 0

        current_sub_matrix = [
            [matrix[r][c], matrix[r][c + 1], matrix[r][c + 2]],
            [matrix[r + 1][c], matrix[r + 1][c + 1], matrix[r + 1][c + 2]],
            [matrix[r + 2][c], matrix[r + 2][c + 1], matrix[r + 2][c + 2]],
        ]

        for row in current_sub_matrix:
            current_sum += sum(row)

        if current_sum > max_sum:
            max_sum = current_sum
            max_sub_matrix = current_sub_matrix

print(f'Sum = {max_sum}')
for row in max_sub_matrix:
    print(' '.join(str(x) for x in row))
