def matrix_generator(size):
    m = []
    for _ in range(size):
        m.append([int(x) if x.isnumeric() else x for x in input().split()])
    return m


def is_outside(r, c, size):
    return r not in range(size) or c not in range(size)


def get_score(r, c, matrix):
    points = 0

    if is_outside(r, c, size):
        return points

    score = matrix[r][c]

    if score is int:
        points += score

    elif score == 'D':
        points += (
                matrix[r][0] +
                matrix[r][6] +
                matrix[0][c] +
                matrix[6][c]
        ) * 2

    elif score == 'T':
        points += (
                matrix[r][0] +
                matrix[r][6] +
                matrix[0][c] +
                matrix[6][c]
        ) * 3

    elif score == 'B':
        return 'winner'

    return points


size = 7
player_one, player_two = input().split(', ')
matrix = matrix_generator(7)
throw = 0

player_one_throws = 0
player_two_throws = 0

player_one_points = 501
player_two_points = 501

one_wins = False
two_wins = False

while True:
    command = input()
    throw += 1
    row, col = (int(x) for x in command[1: len(command) - 1].split(', '))
    score = get_score(row, col, matrix)

    if throw % 2 != 0:
        player_one_throws += 1
        if score == 'winner':
            one_wins = True
            break

        player_one_points -= score
        if player_one_points <= 0:
            one_wins = True
            break

    elif throw % 2 == 0:
        player_two_throws += 1
        if score == 'winner':
            two_wins = True
            break

        player_two_points -= score
        if player_two_points <= 0:
            two_wins = True
            break

if not (one_wins or two_wins):
    if player_one_points < player_two_points:
        one_wins = True
    else:
        two_wins = True

if one_wins:
    print(f'{player_one} won the game with {player_one_throws} throws!')
if two_wins:
    print(f'{player_two} won the game with {player_two_throws} throws!')
