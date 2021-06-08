"Simple class to represent a die"
from mmap import MADV_DONTNEED
from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        random_n = randint(1, self.sides)
        print(random_n)


my_normal_die = Die()
for roll in range(1, 10):
    my_normal_die.roll_die()


ten_sided_die = Die(10)
for roll in range(1, 10):
    my_normal_die.roll_die()


twenty_sided_die = Die(20)
for roll in range(1, 10):
    my_normal_die.roll_die()
