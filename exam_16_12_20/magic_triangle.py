def get_magic_triangle(n):
    triangle = []
    for i in range(n):
        triangle.append([1] * (i + 1))

    for r in range(2, n):
        for c in range(1, len(triangle[r]) - 1):
            triangle[r][c] = triangle[r - 1][c - 1] + triangle[r - 1][c]

    return triangle


get_magic_triangle(10)