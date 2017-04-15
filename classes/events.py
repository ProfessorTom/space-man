class Event:

    def __init__(self, name, key):
        self.name = name
        self.key = key

    def show(self):
        print(self.name + "!!!")
        print("Type " + self.key + " to solve the problem")