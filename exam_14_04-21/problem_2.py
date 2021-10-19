def world_generator(size_of_world: int):
    field = []
    for r in range(size_of_world):
        field.append(input().split())
    return field


def find_player(world, size):
    for r in range(size):
        for c in range(size):
            if world[r][c] == 'P':
                player_r, player_c = r, c
                return player_r, player_c


def step_outside_world(r, c, size):
    if r in range(0, size) and c in range(0, size):
        return False
    return True


def step_into_wall(r, c, world):
    if world[r][c] == 'X':
        return True
    return False


def points_collection(r, c, world, points):
    if world[r][c].isnumeric():
        points += int(world[r][c])
    return points


def path_tracker(r, c, path):
    path.append([r, c])
    return path


steps = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

size = int(input())
field = world_generator(size)
coins = 0
path = []

row, col = find_player(field, size)

while coins < 100:
    row, col = steps[input()](row, col)
    if (
            step_outside_world(row, col, size) or
            step_into_wall(row, col, field)
    ):
        coins *= 0.5
        coins = int(coins)
        break

    coins = points_collection(row, col, field, coins)
    path = path_tracker(row, col, path)

if coins < 100:
    print(f"Game over! You've collected {coins} coins.")

else:
    print(f"You won! You've collected {coins} coins.")

print('Your path:')
for step in path:
    print(step)