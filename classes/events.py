import random

class Event:

    def __init__(self, name, dmg_lo, dmg_hi):
        self.name = name
        self.dmg_lo = dmg_lo
        self.dmg_hi = dmg_hi
        self.dmg = random.randint(dmg_lo, dmg_hi)
        self.rand_words = ["fix", "help", "wer", "djg", "wot"]
        self.len_rand_words = len(self.rand_words) - 1

    def show(self): # Prints the current event and the solution
        print(self.name + "!!!")


    def key_input(self): # Checks user's input against a key

        # Randomize key
        i = random.randint(0, self.len_rand_words)
        random_key = str(random.randint(100, 999)) + self.rand_words[i]

        print("Type " + random_key + " to solve the problem")
        key_input = input()
        return key_input == random_key
