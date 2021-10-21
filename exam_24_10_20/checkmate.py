def board_generator(size_of_world: int):
    field = []
    for r in range(size_of_world):
        field.append(input().split(' '))
    return field


def find_king(world, size):
    for r in range(size):
        for c in range(size):
            if world[r][c] == 'K':
                player_r, player_c = r, c
                return player_r, player_c


def step_outside_board(r, c, size):
    if r in range(0, size) and c in range(0, size):
        return False
    return True


def find_queen(r, c, world):
    return world[r][c] == 'Q'


size = 8
chess_board = board_generator(size)
queens_positions = []

steps = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
    'up_right': lambda r, c: (r - 1, c + 1),
    'up_left': lambda r, c: (r - 1, c - 1),
    'down_right': lambda r, c: (r + 1, c + 1),
    'down_left': lambda r, c: (r + 1, c - 1)
}

for direction in steps:
    row, col = find_king(chess_board, size)

    while True:
        next_row, next_col = steps[direction](row, col)
        if step_outside_board(next_row, next_col, size):
            break

        row, col = next_row, next_col
        if find_queen(row, col, chess_board):
            queens_positions.append([row, col])
            break

if not queens_positions:
    print('The king is safe!')
else:
    for p in queens_positions:
        print(p)











