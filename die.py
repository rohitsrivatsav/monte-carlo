from random import random


class Die:
    def __init__(self, bias=(1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6)):
        self.cdf = [sum(bias[:i + 1]) for i, b in enumerate(bias)]

    def roll(self):
        r = random()
        bools = [r < self.cdf[i] for i in range(6)]
        side = bools.index(True) + 1
        return side
