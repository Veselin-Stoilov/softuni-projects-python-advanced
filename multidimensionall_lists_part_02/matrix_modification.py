def matrix_generator(rows):
    matrix_gn = []
    for _ in range(rows):
        matrix_gn.append([int(x) for x in input().split()])
    return matrix_gn


def matrix_addition(matrix, row, col, value):
    matrix[row][col] += value
    return matrix


def matrix_subtraction(matrix, row, col, value):
    matrix[row][col] -= value
    return matrix


def coordinates_are_valid(number_of_rows, row, col):
    if row in range(0, number_of_rows) and col in range(0, number_of_rows):
        return True
    return False


number_of_rows = int(input())
matrix = matrix_generator(number_of_rows)

while True:
    command = input()
    if command == 'END':
        break

    command = command.split()
    action = command[0]
    row = int(command[1])
    col = int(command[2])
    value = int(command[3])

    if not coordinates_are_valid(number_of_rows, row, col):
        print('Invalid coordinates')
        continue

    if action == 'Add':
        matrix = matrix_addition(matrix, row, col, value)

    elif action == 'Subtract':
        matrix = matrix_subtraction(matrix, row, col, value)

for c in matrix:
    print(' '.join(str(x) for x in c))





