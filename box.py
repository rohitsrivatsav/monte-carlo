from random import randint, choice


class Box:

    def __init__(self):
        self.box = ['red', 'red', 'red', 'red', 'green', 'green', 'green', 'yellow', 'yellow']
        self.interim = []
        self.pick = ''

    def drawmarble(self, drawno):
        if drawno == 0:
            self.pick = choice(self.box)
            self.interim = self.box.copy()
            self.interim.pop(self.box.index(self.pick))
            print(self.pick)
            return self.pick
        else:
            # r = randint(1, len(self.interim))
            # print(self.interim)
            self.pick = choice(self.interim)
            self.interim.pop(self.interim.index(self.pick))
            print(self.pick)
            return self.pick

        # if r <= 4:
        #     self.pick = 'red'
        # elif r <= 6:
        #     self.pick = 'yellow'
        # else:
        #     self.pick = 'green'
        # self.update_probability(self.pick)
        # return self.pick

# b = Box()
# for j in range(100):
#     print("this is J")
#     print(j)
#     for i in range(5):
#         print(i)
#         b.drawmarble(i)
