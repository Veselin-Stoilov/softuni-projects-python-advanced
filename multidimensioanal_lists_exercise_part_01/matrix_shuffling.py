def matrix_creator():
    matrix = []
    for _ in range(n):
        matrix.append(input().split())
    return matrix


def elements_swap():
    matrix[coordinates[0]][coordinates[1]], matrix[coordinates[2]][coordinates[3]] = \
        matrix[coordinates[2]][coordinates[3]], matrix[coordinates[0]][coordinates[1]]


def valid_command():
    if command[0] == 'swap' and len(command) == 5:
        coordinates = [int(x) for x in command[1:]]
        if (coordinates[0] or coordinates[2]) < n or (coordinates[1] or coordinates[3]) < m:
            return True


n, m = (int(x) for x in input().split())
matrix = matrix_creator()

while True:
    command = input()
    if command == 'END':
        break

    command = command.split()

    if valid_command():
        coordinates = [int(x) for x in command[1:]]
        elements_swap()

        for row in matrix:
            print(' '.join(row))

    else:
        print('Invalid input!')

