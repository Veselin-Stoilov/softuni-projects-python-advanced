def matrix_creator():
    matrix = []
    for _ in range(n):
        matrix.append([int(x) for x in input().split(', ')])
    return matrix


n, m = (int(x) for x in (input().split(', ')))

matrix = matrix_creator()
square_sum_dict = {}

for r in range(n - 1):
    for c in range(m - 1):
        current_sum = matrix[r][c] + matrix[r][c + 1] + matrix[r + 1][c] + matrix[r + 1][c + 1]
        square_sum_dict[current_sum] = ((matrix[r][c], matrix[r][c + 1]), (matrix[r + 1][c], matrix[r + 1][c + 1]))

max_sum = max(square_sum_dict)

for row in square_sum_dict[max_sum]:
    print(row[0], row[1])

print(max_sum)

