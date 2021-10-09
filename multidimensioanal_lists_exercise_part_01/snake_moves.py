def snake_matrix_generator(string):
    """
    this function generates a matrix from a string
    simulating a snake move
    """
    matrix = []
    string_index = 0

    for r in range(n):
        column = ''

        for c in range(m):
            column += string[string_index]
            string_index = (string_index + 1) % len(string)

        if r % 2 != 0:
            column = column[::-1]

        matrix.append(column)

    return matrix


n, m = (int(x) for x in input().split())
word = input()

snake_matrix = snake_matrix_generator(word)

for row in snake_matrix:
    print(row)




