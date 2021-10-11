def matrix_generator(matrix_size):
    matrix_gn = []
    for _ in range(matrix_size):
        matrix_gn.append(list(input()))
    return matrix_gn


def framing_of_matrix(matrix):
    """
    this function will frame the main matrix with
    two additional layers of empty cells, so the
    possible moves would never go out of scope
    :param: main matrix:
    :return: framed matrix
    """
    fm = []

    for r in range(len(matrix) + 4):
        row = []
        for c in range(len(matrix) + 4):
            if r in range(0, 2) or r in range(len(matrix) + 2, len(matrix) + 4) or c in range(0, 2) or c in range(len(matrix) + 2, len(matrix) + 4):
                row.append(None)
            else:
                row.append(matrix[r - 2][c - 2])
        fm.append(row)
    return fm


size_of_board = int(input())
m = matrix_generator(size_of_board)
fr_mat = framing_of_matrix(m)
attack_is_possible = True
removed_knights = 0

while attack_is_possible:

    attack_count = 0
    max_attacks = 0
    attack_is_possible = False
    possible_moves = []

    for r in range(2, len(fr_mat) - 2):
        for c in range(2, len(fr_mat) - 2):
            if fr_mat[r][c] == 'K':
                possible_moves = [
                    fr_mat[r - 2][c - 1], fr_mat[r - 2][c + 1],
                    fr_mat[r - 1][c - 2], fr_mat[r - 1][c + 2],
                    fr_mat[r + 1][c - 2], fr_mat[r + 1][c + 2],
                    fr_mat[r + 2][c - 1], fr_mat[r + 2][c + 1],
                ]

                attack_count = possible_moves.count('K')

                if max_attacks < attack_count:
                    max_attacks = attack_count
                    best_knight_row, best_knight_col = r, c
                    attack_is_possible = True

    if attack_is_possible:
        fr_mat[best_knight_row][best_knight_col] = '0'
        removed_knights += 1


print(removed_knights)



