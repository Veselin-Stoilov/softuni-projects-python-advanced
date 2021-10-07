def matrix_creator():
    matrix = []
    for r in range(n):
        column = []
        for c in range(m):
            column.append(chr(97 + r) + chr(97 + r + c) + chr(97 + r))
        matrix.append(column)
    return matrix


n, m = (int(x) for x in input().split())
matrix = matrix_creator()

for row in matrix:
    print(' '.join(row))


