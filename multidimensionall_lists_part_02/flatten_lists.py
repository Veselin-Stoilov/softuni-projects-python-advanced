from collections import deque


def matrix_generator(string):
    matrix_gn = deque()
    line = string.split('|')
    for column in line:
        column = ' '.join([x for x in column.split() if x != ' '])
        matrix_gn.appendleft(column)
    return matrix_gn


matrix = matrix_generator(input())

print(' '.join(matrix))