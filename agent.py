import random
import numpy as np
from environment import get_valid_moves, get_initial_state
from collections import defaultdict


def default_q():
    return [0, 0, 0, 0, 0, 0, 0, 0, 0]


def parse_state(state):
    return ''.join(map(str,list(np.array(state).flatten())))


class Agent:
    def __init__(self, tile=None):
        self.tile = tile

    def get_action(self, state):
        return random.choice(get_valid_moves(state))


class LearningAgent(Agent):
    def __init__(self, tile=None):
        Agent.__init__(self, tile)
        self.Q = defaultdict(default_q)
        self.alpha = 0.5

    def learn(self, turns):
        for turn in turns:
            parsed_state = parse_state(turn['st'])
            old_q = self.Q[parsed_state][turn['a']]

            if not turn['st1']:
                reward = turn['r']
            else:
                parsed_state_t1 = parse_state(turn['st1'])
                reward = np.array(self.Q[parsed_state_t1]).max()

            self.Q[parsed_state][turn['a']] = old_q + self.alpha * (reward - old_q)

    def get_action(self, state):
        valid_moves = get_valid_moves(state)

        if random.random() < 0.1:
            return Agent.get_action(self, state)

        parsed_state = parse_state(state)
        array = np.array(self.Q[parsed_state]).argsort()
        predicted_moves = list(array)

        for i in reversed(range(9)):
            # get the index of the tempted move
            tempted_move = predicted_moves.index(i)
            # if the top priority move is among valid moves
            if tempted_move in valid_moves:
                # take this move
                return tempted_move
