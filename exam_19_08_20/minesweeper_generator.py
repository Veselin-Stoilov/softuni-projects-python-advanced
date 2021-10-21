def board_generator(size: int):
    field = []
    for r in range(size):
        field.append([None] * size)
    return field


def place_bombs(matrix, bombs):
    for _ in range(bombs):
        bomb_position = input()
        r, c = (int(x) for x in bomb_position[1: len(bomb_position) - 1].split(', '))
        matrix[r][c] = '*'
    return matrix


def is_outside(r, c, size):
    if r in range(0, size) and c in range(0, size):
        return False
    return True


def final_built(board, size):
    surround_check = {
        'right': lambda r, c: (r, c + 1),
        'left': lambda r, c: (r, c - 1),
        'up': lambda r, c: (r - 1, c),
        'down': lambda r, c: (r + 1, c),
        'up_right': lambda r, c: (r - 1, c + 1),
        'up_left': lambda r, c: (r - 1, c - 1),
        'down_right': lambda r, c: (r + 1, c + 1),
        'down_left': lambda r, c: (r + 1, c - 1)
    }

    for row in range(size):
        for col in range(size):
            if board[row][col] == '*':
                continue

            mines_found = 0
            for check in surround_check:
                mine_check_r, mine_check_c = surround_check[check](row, col)

                if is_outside(mine_check_r, mine_check_c, size):
                    continue

                if board[mine_check_r][mine_check_c] == '*':
                    mines_found += 1
            board[row][col] = mines_found
    return board


size = int(input())
bombs = int(input())
board = board_generator(size)
board = place_bombs(board, bombs)

board = final_built(board, size)

for line in board:
    line = [str(x) if str(x).isnumeric() else x for x in line]
    print(' '.join(line))



