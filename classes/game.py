import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLING = '\033[4m'

class Energy():
    def __init__(self, current):
        self.current = current
        self.max = 100

    def display(self):
        i = 0
        print("\nCurrent Energy: " + str(self.current) + "/100")
        while i < (self.current/5):
            sys.stdout.write(bcolors.OKGREEN + "█" + bcolors.ENDC)
            i += 1
        while i < 20:
            sys.stdout.write(bcolors.FAIL + "█" + bcolors.ENDC)
            i += 1
        print("\n")