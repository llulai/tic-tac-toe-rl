from copy import deepcopy


def get_initial_state():
    return [[0 for _ in range(3)] for __ in range(3)]


def get_valid_moves(state):
    if get_winner(state):
        return False
    else:
        valid_moves = []
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    valid_moves.append(i*3 + j)

        return valid_moves


def make_move(state, action, tile):
    new_state = deepcopy(state)
    i = int(action / 3)
    j = action % 3
    new_state[i][j] = tile

    return new_state


def get_winner(state):
    # check horizontal
    for i in range(len(state)):
        if state[i][0] == state[i][1] == state[i][2] != 0:
            return state[i][0]

    # check verticals
    for j in range(len(state[0])):
        if state[0][j] == state[1][j] == state[2][j] != 0:
            return state[0][j]

    # check \ diagonal
    if state[0][0] == state[1][1] == state[2][2] != 0:
        return state[0][0]

    # check \ diagonal
    if state[0][2] == state[1][1] == state[2][0] != 0:
        return state[1][1]

    return 0
