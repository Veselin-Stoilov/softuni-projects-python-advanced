def board_generator(size: int):
    field = []
    for r in range(size):
        field.append([0] * size)
    return field


def player_one_move(matrix, size):
    print('')
    c = int(input('Player [1], please choose a column: \n'))
    print('')
    c -= 1
    for r in range(size):
        if is_outside(r, c, size):
            print('Invalid input! Try again.')
            return 'Invalid', 'Invalid', matrix
        if matrix[r][c] == 0:
            matrix[r][c] = 1
            return r, c, matrix
        if r == size - 1:
            print('Invalid input! Try again.')
            return 'Invalid', 'Invalid', matrix


def player_two_move(matrix, size):
    print('')
    c = int(input('Player [2], please choose a column: \n'))
    print('')
    c -= 1
    for r in range(size):
        if is_outside(r, c, size):
            print('Invalid input! Try again.')
            return 'Invalid', 'Invalid', matrix
        if matrix[r][c] == 0:
            matrix[r][c] = 2
            return r, c, matrix
        if r == size - 1:
            print('Invalid input! Try again.')
            return 'Invalid', 'Invalid', matrix


def is_outside(r, c, size):
    if r in range(0, size) and c in range(0, size):
        return False
    return True


def is_winner(r, c, board, line):
    """
    this function returns True
    if player wins the game
    with his last move
    """
    horizontal = {
        'right': lambda r, c: (r, c + 1),
        'left': lambda r, c: (r, c - 1),
    }
    vertical = {
        'up': lambda r, c: (r - 1, c),
        'down': lambda r, c: (r + 1, c),
    }
    right_diagonal = {
        'up_right': lambda r, c: (r - 1, c + 1),
        'down_left': lambda r, c: (r + 1, c - 1)
    }
    left_diagonal = {
        'up_left': lambda r, c: (r - 1, c - 1),
        'down_right': lambda r, c: (r + 1, c + 1),
    }
    current_player = board[r][c]

    slots_horizontal = 1
    slots_vertical = 1
    slots_right_diagonal = 1
    slots_left_diagonal = 1
    for d in horizontal:
        next_r, next_c = horizontal[d](r, c)
        if is_outside(next_r, next_c, size):
            continue
        while True:
            if board[next_r][next_c] == current_player:
                slots_horizontal += 1
                if slots_horizontal == line:  # winning condition
                    return True
                next_r, next_c = horizontal[d](next_r, next_c)
                if is_outside(next_r, next_c, size):
                    break
            else:
                break

    for d in vertical:
        next_r, next_c = vertical[d](r, c)
        if is_outside(next_r, next_c, size):
            continue
        while True:
            if board[next_r][next_c] == current_player:
                slots_vertical += 1
                if slots_vertical == line:  # winning condition
                    return True
                next_r, next_c = vertical[d](next_r, next_c)
                if is_outside(next_r, next_c, size):
                    break
            else:
                break

    for d in right_diagonal:
        next_r, next_c = right_diagonal[d](r, c)
        if is_outside(next_r, next_c, size):
            continue
        while True:
            if board[next_r][next_c] == current_player:
                slots_right_diagonal += 1
                if slots_right_diagonal == line:  # winning condition
                    return True
                next_r, next_c = right_diagonal[d](next_r, next_c)
                if is_outside(next_r, next_c, size):
                    break
            else:
                break

    for d in left_diagonal:
        next_r, next_c = left_diagonal[d](r, c)
        if is_outside(next_r, next_c, size):
            continue
        while True:
            if board[next_r][next_c] == current_player:
                slots_left_diagonal += 1
                if slots_left_diagonal == line:  # winning condition
                    return True
                next_r, next_c = left_diagonal[d](next_r, next_c)
                if is_outside(next_r, next_c, size):
                    break
            else:
                break
    return False


size = 7  # size of the board
slots_to_win = 3  # humber of elements in line to win the game
board = board_generator(size)
column_indexes = [1, 2, 3, 4, 5, 6, 7]
print(column_indexes)
for r in reversed(board):
    print(r)
players = [1, 2]


while True:

    if players[0] == 1:
        row, col, board = player_one_move(board, size)
        if row == 'Invalid':
            continue

        print(column_indexes)
        for r in reversed(board):
            print(r)
            players = [2, 1]
        if is_winner(row, col, board, slots_to_win):
            print('Player [1] wins, CONGRATULATIONS!')
            break
    if players[0] == 2:
        row, col, board = player_two_move(board, size)
        if row == 'Invalid':
            player_two_invalid_move = True
            continue
        print(column_indexes)
        for r in reversed(board):
            print(r)
            players = [1, 2]
        if is_winner(row, col, board, slots_to_win):
            print('Player [2] wins, CONGRATULATIONS!')
            break

