import random
import threading
import time

class Event:

    def __init__(self, name, dmg_lo, dmg_hi, rand_words):
        self.name = name
        self.dmg_lo = dmg_lo
        self.dmg_hi = dmg_hi
        self.dmg = random.randint(dmg_lo, dmg_hi)
        self.rand_words = rand_words
        self.len_rand_words = len(self.rand_words) - 1

    def show(self): # Prints the current event and the solution
        print(self.name + "!!!")

    def random_key(self): # Generates a random keycode

        i = random.randint(0, self.len_rand_words)
        random_key = str(random.randint(100, 999)) + self.rand_words[i]

        return random_key
