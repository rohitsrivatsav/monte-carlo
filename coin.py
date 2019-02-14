from random import random


class Coin:
    def __init__(self, bias=0.5):
        self.bias = bias

    def flip(self):
        return random() < self.bias
