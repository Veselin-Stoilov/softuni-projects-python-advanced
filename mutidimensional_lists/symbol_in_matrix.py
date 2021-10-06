def matrix_creator():
    matrix = []
    for _ in range(n):
        matrix.append(list(input()))
    return matrix


n = int(input())

matrix = matrix_creator()
symbol_found = False
searched_symbol = input()

for row in range(n):
    if searched_symbol in matrix[row]:
        symbol_found = True
        print((row, matrix[row].index(searched_symbol)))
        break

if not symbol_found:
    print(f'{searched_symbol} does not occur in the matrix')