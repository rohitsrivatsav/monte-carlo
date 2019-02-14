from coin import Coin


class Experiment:
    def flip_coin_x_times(self, x):
        # return the probability of head
        c = Coin()
        return sum((c.flip() for _ in range(x))) / x

    def flip_coin_2x_n_times(self, n):
        c = Coin()
        experiments = [sum([c.flip(), c.flip()]) == 2 for _ in range(n)]
        return sum(experiments) / n

    def flip_coin_with_pattern_n_times(self, pattern, n, flips, bias=0.5):
        c = Coin(bias)
        experiments = [[c.flip() for f in range(flips)] == pattern for e in range(n)]
        return sum(experiments) / n
