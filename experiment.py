from coin import Coin


class Experiment:
    def flip_coin_x_times(self, x):
        # return the probability of head
        c = Coin()
        return sum((c.flip() for _ in range(x))) / x
