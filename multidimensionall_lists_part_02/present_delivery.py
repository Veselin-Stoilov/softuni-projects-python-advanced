def neighbourhood_generator(size_of_world: int):
    matrix = []
    for r in range(size_of_world):
        matrix.append(input().split())
    return matrix


def santa_position(world, size):
    for r in range(size):
        for c in range(size):
            if world[r][c] == 'S':
                world[r][c] = '-'
                player_r, player_c = r, c
                return player_r, player_c


def nice_kids_count(world):
    kids = 0
    for r in world:
        kids += r.count('V')
    return kids


def position_outside_world(r, c, size):
    if r in range(0, size) and c in range(0, size):
        return False
    return True


def cookie(r, c, world, presents):
    if world[r][c + 1] in ('X', 'V'):
        world[r][c + 1] = '-'
        presents -= 1
    if world[r][c - 1] in ('X', 'V'):
        world[r][c - 1] = '-'
        presents -= 1
    if world[r + 1][c] in ('X', 'V'):
        world[r + 1][c] = '-'
        presents -= 1
    if world[r - 1][c] in ('X', 'V'):
        world[r - 1][c] = '-'
        presents -= 1
    return world, presents


moves = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

gifts = int(input())
size = int(input())
neighbourhood = neighbourhood_generator(size)
initial_nice_kids = nice_kids_count(neighbourhood)
nice_kids = initial_nice_kids
mission_complete = False

santa_row, santa_col = santa_position(neighbourhood, size)

while True:
    command = input()
    if command == 'Christmas morning':
        break
    next_step_row, next_step_col = moves[command](santa_row, santa_col)

    if position_outside_world(next_step_row, next_step_col, size):
        continue
    santa_row, santa_col = next_step_row, next_step_col

    if neighbourhood[santa_row][santa_col] == 'X':
        neighbourhood[santa_row][santa_col] = '-'
        continue

    if neighbourhood[santa_row][santa_col] == 'V':
        neighbourhood[santa_row][santa_col] = '-'
        gifts -= 1

    elif neighbourhood[santa_row][santa_col] == 'C':
        neighbourhood[santa_row][santa_col] = '-'
        world, gifts = cookie(santa_row, santa_col, neighbourhood, gifts)

    nice_kids = nice_kids_count(neighbourhood)
    if nice_kids == 0:
        mission_complete = True
        break

    if gifts == 0:
        print('Santa ran out of presents!')
        break

neighbourhood[santa_row][santa_col] = 'S'

for r in neighbourhood:
    print(' '.join(r))

if mission_complete:
    print(f"Good job, Santa! {initial_nice_kids} happy nice kid/s.")

else:
    print(f"No presents for {nice_kids} nice kid/s.")






