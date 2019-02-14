from random import randint


class Dice:
    def __init__(self):
        self.one = 30
        self.two = 35
        self.three = 40
        self.four = 70
        self.five = 80
        self.six = 100

    def roll(self):
        r = randint(0, 100)
        if(r <= self.one):
            return 1
        elif(r > self.one and r <= self.two):
            return 2
        elif(r > self.two and r <= self.three):
            return 3
        elif(r > self.three and r <= self.four):
            return 4
        elif(r > self.four and r <= self.five):
            return 5
        elif(r > self.five and r <= self.six):
            return 6
