import random

from agent import Agent
from environment import get_initial_state, get_valid_moves, make_move
from itertools import cycle

def simulate(games=10):
    agents = [Agent(1), Agent(-1)]

    players = cycle(agents)

    for _ in range(random.randrange(2)):
        current_player = next(players)

    for iteration in range(games):
        state = get_initial_state()

        while get_valid_moves(state):
            current_player = next(players)
            initial_state = state
            action = current_player.get_action(state)
            state = make_move(state, action, current_player.tile)

            print(state)

if __name__ == '__main__':
    simulate(1)
