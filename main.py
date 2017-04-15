import random
from classes.events import Event
from classes.game import bcolors
from classes.game import Energy

running = True
energy = Energy(100)

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

# Defining Events
low_air = Event("Low Air", 3, 7)
asteroid = Event("Asteroid", 10, 20)
black_hole = Event("Black hole", 15, 30)

# Creating a list of events
event_list = [low_air, asteroid, black_hole]
num_events = len(event_list) - 1 # number of events

# Start of game
print(instructions)
while running:

    if energy.current <= 0:
        print(bcolors.FAIL + '\nGame Over! Your ship sustained too much damage.\n' + bcolors.ENDC)
        running = False
        break

    energy.display()

    #print(bcolors.OKBLUE + '\nCurrent energy level is ' + str(energy) + '%' + bcolors.ENDC)

    chance = random.randint(0, num_events) # Creates random number

    current_event = event_list[chance] # randomly chooses current event
    current_event.show()

    if current_event.key_input(): # Checks if correct key solution was entered
        print(bcolors.OKGREEN + "Problem solved!" + bcolors.ENDC)
        print(bcolors.OKGREEN + "Great work!" + bcolors.ENDC)
        continue
    else:
        energy.current -= current_event.dmg
        print(bcolors.FAIL + "Incorrect!" + bcolors.ENDC)
        print(bcolors.FAIL + "You have lost " + str(current_event.dmg) + " energy" + bcolors.ENDC)
        continue