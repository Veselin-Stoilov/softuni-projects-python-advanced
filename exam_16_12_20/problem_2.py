def world_generator(size_of_world: int):
    field = []
    for r in range(size_of_world):
        field.append(list(input()))
    return field


def find_player(world, size):
    for r in range(size):
        for c in range(size):
            if world[r][c] == 'P':
                world[r][c] = '-'
                player_r, player_c = r, c
                return player_r, player_c


def step_outside_world(r, c, size):
    if r in range(0, size) and c in range(0, size):
        return False
    return True


def letters_collector(r, c, world, string):
    if world[r][c].isalpha():
        string += world[r][c]
    return string


def path_tracker(r, c, world):
    world[r][c] = '-'
    return world


string = input()
size = int(input())
world = world_generator(size)
moves = int(input())

steps = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

row, col = find_player(world, size)

for _ in range(moves):
    next_step = input()
    next_row, next_col = steps[next_step](row, col)

    if step_outside_world(next_row, next_col, size):
        if string:
            string = string[:-1]
            continue

    row, col = next_row, next_col

    string = letters_collector(row, col, world, string)

    world = path_tracker(row, col, world)

world[row][col] = 'P'

print(string)

for r in world:
    print(''.join(r))











