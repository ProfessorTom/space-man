import random
from classes.events import Event
from classes.game import Energy

running = True
energy = Energy(100)
score = 0

instructions = """
********************************************************************************

                                    Space Life

********************************************************************************


Welcome to the Space Life game!
In this game you will encounter many problems
astronauts experience in space.
When you encounter a problem at a random point in
this game, you will need to enter a random key code
in order to pass the problem unhurt.
"""

# Event Key-Codes
low_air_keys = ["air", "aero", "oxy"]
asteroid_keys = ["rocks", "meteor", "meteorite", "collide"]
black_hole_keys = ["wormhole", "blackhole", "timespace", "gravity"]


# Defining Events
low_air = Event("Low Air", 3, 7, low_air_keys)
asteroid = Event("Asteroid", 10, 20, asteroid_keys)
black_hole = Event("Black hole", 15, 30, black_hole_keys)

# Creating a list of events
event_list = [low_air, asteroid, black_hole]
num_events = len(event_list) - 1 # number of events

# Start of game
print(instructions)
while running:

    if energy.current <= 0:
        print('\nGame Over! Your ship sustained too much damage.\n')
        energy.display()
        print("Your score is " + score)
        running = False
        break

    energy.display()

    chance = random.randint(0, num_events) # Creates random number

    current_event = event_list[chance] # randomly chooses current event
    current_event.show()

    if current_event.key_input(): # Checks if correct key solution was entered
        print("Problem solved!")
        print("Great work!")
        score += 10
        continue
    else:
        energy.current -= current_event.dmg
        print("Incorrect!")
        print("You have lost " + str(current_event.dmg) + " energy")
        score += 1
        continue