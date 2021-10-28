def create_line(n: int):
    line = []
    for el in range(1, n + 1):
        line.append(el)
    return line


def create_triangle(n: int):
    matrix = []
    for i in range(1, n + 1):
        row = create_line(i)
        matrix.append(row)
    for i in range(n - 1, 0, -1):
        row = create_line(i)
        matrix.append(row)
    return matrix


def triangle_as_str(size):
    string = ''
    triangle = create_triangle(size)
    for r in triangle:
        r = [str(x) for x in r]
        string += f'{" ".join(r)}\n'
    return string

