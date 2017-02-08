import random
from environment import get_valid_moves

class Agent:
    def __init__(self, tile=None):
        self.tile = tile

    def get_action(self, state):
        return random.choice(get_valid_moves(state))


class LearningAgent(Agent):
    def __init__(self, tile=None):
        Agent.__init__(self, tile)

    def learn(self, state, action, reward):
        pass