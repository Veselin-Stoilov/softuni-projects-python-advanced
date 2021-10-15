def world_generator(size_of_world: int):
    field = []
    for r in range(size_of_world):
        field.append(input().split())
    return field


def find_alice(world, size):
    for r in range(size):
        for c in range(size):
            if world[r][c] == 'A':
                world[r][c] = '*'
                alice_r, alice_c = r, c
                return alice_r, alice_c


def step_outside_world(r, c, size):
    if r in range(0, size) and c in range(0, size):
        return False
    return True


def step_into_rabbit_hole(r, c, world):
    if world[r][c] == 'R':
        world[r][c] = '*'
        return True
    return False


def tea_bags_collection(r, c, world, tea_bags):
    if world[r][c].isnumeric():
        tea_bags += int(world[r][c])
    return tea_bags


def path_tracker(r, c, world):
    world[r][c] = '*'
    return world


size = int(input())
world = world_generator(size)

tea_bags = 0

steps = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}

row, col = find_alice(world, size)

while True:
    next_step = input()
    row, col = steps[next_step](row, col)

    if step_outside_world(row, col, size) or step_into_rabbit_hole(row, col, world):
        print("Alice didn't make it to the tea party.")
        break

    tea_bags = tea_bags_collection(row, col, world, tea_bags)
    world = path_tracker(row, col, world)

    if tea_bags >= 10:
        print("She did it! She went to the party.")
        break

for r in world:
    print(' '.join(r))