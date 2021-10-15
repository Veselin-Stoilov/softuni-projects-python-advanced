def field_generator(size_of_world: int):
    field = []
    for r in range(size_of_world):
        field.append(input().split())
    return field


def shooter_position(world, size):
    for r in range(size):
        for c in range(size):
            if world[r][c] == 'A':
                player_r, player_c = r, c
                return player_r, player_c


def number_of_targets(world):
    targets = 0
    for r in world:
        targets += r.count('x')
    return targets


def position_outside_world(r, c, size):
    if r in range(0, size) and c in range(0, size):
        return False
    return True


def step_over_target(r, c, world):
    if world[r][c] == 'x':
        return True
    return False


moves = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

size = 5
field = field_generator(size)
number_of_moves = int(input())
targets_shot = 0
targets_hit = []
targets = number_of_targets(field)
player_row, player_col = shooter_position(field, size)

for _ in range(number_of_moves):
    command = input().split()
    action = command[0]
    direction = command[1]

    if action == 'move':
        steps = int(command[2])
        for step in range(steps):
            next_player_row, next_player_col = moves[direction](player_row, player_col)
            if position_outside_world(next_player_row, next_player_col, size) or\
               step_over_target(next_player_row, next_player_col, field):
                break
            player_row, player_col = next_player_row, next_player_col
    elif action == 'shoot':
        bullet_row, bullet_col = player_row, player_col
        while True:
            next_bullet_row, next_bullet_col = moves[direction](bullet_row, bullet_col)

            if position_outside_world(next_bullet_row, next_bullet_col, size):
                break
            bullet_row, bullet_col = next_bullet_row, next_bullet_col

            if field[bullet_row][bullet_col] == 'x':
                targets_shot += 1
                targets_hit.append([bullet_row, bullet_col])
                field[bullet_row][bullet_col] = '.'
                break

    if targets_shot == targets:
        print(f"Training completed! All {targets} targets hit.")
        break

if targets_shot < targets:
    missed_targets = targets - targets_shot
    print(f"Training not completed! {missed_targets} targets left.")

for t in targets_hit:
    print(t)







