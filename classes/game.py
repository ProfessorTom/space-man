import sys

class Energy():
    def __init__(self, current):
        self.current = current
        self.max = 100

    def display(self):
        i = 0
        if self.current <= 0:
            self.current = 0
        print("\nCurrent Energy: " + str(self.current) + "/100")
        while i < (self.current/5):
            sys.stdout.write("█")
            i += 1
        while i < 20:
            sys.stdout.write("_")
            i += 1
        sys.stdout.write("|")
        print("\n")