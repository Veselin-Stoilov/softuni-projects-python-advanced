def field_generator(size_of_field):
    field = []
    for r in range(size_of_field):
        field.append([int(x) if x.isnumeric() else x for x in input().split()])
    return field


def starting_position(field):
    for r in range(size_of_field):
        if 'B' in field[r]:
            bunny_r, bunny_c = r, field[r].index('B')
            return bunny_r, bunny_c


def sum_up(field, bunny_r, bunny_c):
    sum_of_eggs = 0
    path_tracker = []
    for r in range(bunny_r - 1, -1, -1):
        if field[r][bunny_c] == 'X':
            break
        sum_of_eggs += field[r][bunny_c]
        path_tracker.append([r, bunny_c])
    return sum_of_eggs, path_tracker


def sum_down(field, bunny_r, bunny_c):
    sum_of_eggs = 0
    path_tracker = []
    for r in range(bunny_r + 1, len(field)):
        if field[r][bunny_c] == 'X':
            break
        sum_of_eggs += field[r][bunny_c]
        path_tracker.append([r, bunny_c])
    return sum_of_eggs, path_tracker


def sum_right(field, bunny_r, bunny_c):
    sum_of_eggs = 0
    path_tracker = []
    for c in range(bunny_c + 1, len(field)):
        if field[bunny_r][c] == 'X':
            break
        sum_of_eggs += field[bunny_r][c]
        path_tracker.append([bunny_r, c])
    return sum_of_eggs, path_tracker


def sum_left(field, bunny_r, bunny_c):
    sum_of_eggs = 0
    path_tracker = []
    for c in range(bunny_c - 1, -1, -1):
        if field[bunny_r][c] == 'X':
            break
        sum_of_eggs += field[bunny_r][c]
        path_tracker.append([bunny_r, c])
    return sum_of_eggs, path_tracker


size_of_field = int(input())

field = field_generator(size_of_field)

bunny_r, bunny_c = starting_position(field)  # position of bunny in the matrix

"""
Next we calculate the collected eggs sum and track the path in all four directions.
"""
max_sum_up, path_up = sum_up(field, bunny_r, bunny_c)[0], sum_up(field, bunny_r, bunny_c)[1]
max_sum_down, path_down = sum_down(field, bunny_r, bunny_c)[0], sum_down(field, bunny_r, bunny_c)[1]
max_sum_right, path_right = sum_right(field, bunny_r, bunny_c)[0], sum_right(field, bunny_r, bunny_c)[1]
max_sum_left, path_left = sum_left(field, bunny_r, bunny_c)[0], sum_left(field, bunny_r, bunny_c)[1]

"""
Then we place the sum results in a dictionary: directions_sum{}
"""
directions_sums = {
    max_sum_up: ['up', path_up],
    max_sum_down: ['down', path_down],
    max_sum_right: ['right', path_right],
    max_sum_left: ['left', path_left],
           }

print(directions_sums[max(directions_sums)][0])

for coordinates in directions_sums[max(directions_sums)][1]:
    print(coordinates)

print(max(directions_sums))


