import random

from agent import Agent, LearningAgent
from environment import get_initial_state, get_valid_moves, make_move, get_winner
from itertools import cycle


def simulate(games=10, log_every=100):
    results = []
    won = 0
    agents = [LearningAgent(1), Agent(-1)]

    players = cycle(agents)

    for _ in range(random.randrange(2)):
        current_player = next(players)

    for iteration in range(1, games + 1):
        state = get_initial_state()

        current_game = []

        while get_valid_moves(state):
            current_player = next(players)
            initial_state = state
            action = current_player.get_action(state)
            state = make_move(state, action, current_player.tile)

            turn = {
                'st': initial_state,
                'a': action,
                'st1': state
            }

            if current_player.tile == 1:
                current_game.append(turn)


        # clean game
        reward = get_winner(state)
        current_game[-1]['r'] = reward
        current_game[-1]['st1'] = None

        # log
        if reward > 0:
            won += 1

        if iteration % log_every == 0:
            print('won %s games out of %s' %(won, log_every))
            won = 0

        # learn

        agents[0].learn(current_game)

        results.append(current_game)

    return agents[0]



if __name__ == '__main__':
    simulate(1000)
