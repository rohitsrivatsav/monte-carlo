from coin import Coin
from dice import Dice
from box import Box


class Experiment:
    def flip_coin_x_times(self, x):
        # returns probability of head
        c = Coin()
        return sum([c.flip() for _ in range(x)]) / x

    # Inst
    def flip_coin_2x_n_times(self, n):
        c = Coin()
        experiments = [sum([c.flip(), c.flip()]) == 2 for _ in range(n)]
        return sum(experiments) / n

    # def flip_biased_coin_4x_n_times(self, n):
    #     c = Coin()
    #     experiments = [sum([c.biasedflip(), c.biasedflip(), c.biasedflip(), c.biasedflip()]) == 4 for _ in range(n)]
    #     return sum(experiments) / n

    def flip_coin_1t1h1t2h_n_times(self, n):
        c = Coin()
        experiments = 0
        for _ in range(n):
            if(c.flip() == 0 and c.flip() == 1 and c.flip() == 0 and c.flip() == 1 and c.flip() == 1):
                experiments += 1
        return experiments / n

    def flip_coin_with_pattern_n_times(self, pattern, n, flips):
        c = Coin()
        experiments = [[c.flip() for f in range(flips)] == pattern for e in range(n)]
        return sum(experiments) / n

    def biased_flip_coin_with_pattern_n_times(self, pattern, n, flips):
        c = Coin(0.3)
        experiments = [[c.flip() for f in range(flips)] == pattern for e in range(n)]
        return sum(experiments) / n

    def roll_dice_4x_times(self, pattern, n, rolls):
        d = Dice()
        experiments = [[d.roll() for f in range(rolls)] in pattern for e in range(n)]
        return sum(experiments) / n

    def draw_marbles_from_box(self, pattern, draws, simulations):
        b = Box()
        # sequence_of_colors = ['red', 'green', 'yellow', 'red', 'red']
        experiments = [[b.drawmarble(d) for d in range(draws)] == pattern for d in range(simulations)]
        # probability = b.boxdict[b.pick] / b.total
        return sum(experiments) / simulations
