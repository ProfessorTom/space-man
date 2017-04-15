import random
from classes.events import Event

print('Welcome to the game!')

energy = 100

# Defining Events
low_air = Event("Low Air", "ghA")
asteroid = Event("Asteroid", "aRu")
black_hole = Event("Black hole", "Oyn")

event_list = [low_air, asteroid, black_hole]
num_events = len(event_list) # number of events

while energy > 0:

    print('\nCurrent energy level is ' + str(energy) + '%')

    chance = random.randint(0, num_events) # Creates random number

    event_list[chance].show() # Prints the current event

    if event_list[chance].key_input(): # Checks if correct key solution was entered
        print("Problem solved!")
        print("Great work!")
    else:
        energy -= 10
        print("Incorrect!")
        print("You have lost energy")

    if energy <= 0:
        print('Game Over! Your ship sustained too much damage.')