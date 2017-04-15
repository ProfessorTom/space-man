class Event:

    def __init__(self, name, key):
        self.name = name
        self.key = key

    def show(self): # Prints the current event and the solution
        print(self.name + "!!!")
        print("Type " + self.key + " to solve the problem")

    def key_input(self): #
        key_input = input()
        return key_input == self.key
