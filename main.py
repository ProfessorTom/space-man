import random
import time
from threading import Timer
from classes.events import Event
from classes.game import Energy

def input_with_timeout(x): # function for inputting with a time limit

    def time_up():
        print ("\nTime up! Enter any key to continue.")

    t = Timer(x,time_up) # x is amount of time in seconds
    t.start()
    try:
        answer = input("Enter key: ")
    except Exception:
        print('pass\n')
        answer = None

    if answer != True:
        t.cancel()       # time_up will not execute(so, no skip)

    return answer

running = True
energy = Energy(100)
score = 0
successful_loops = 0

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
begin = input("Press any key to continue")

while running:

    # Checking if you are dead
    if energy.current <= 0:
        print('\nGame Over! Your ship sustained too much damage.\n')
        energy.display()
        print("Your score is " + str(score))
        running = False
        time.sleep(5)
        break

    # Displaying your current energy
    energy.display()
    time.sleep(1)

    chance = random.randint(0, num_events) # Creates random number

    # Selects random event
    current_event = event_list[chance]
    current_event.show()

    # Create a random key
    key = current_event.generate_key()
    print("Type " + key + " to solve the problem")

    # Getting user input
    answer = input_with_timeout(5) # number in parenthesis is how many seconds you have left

    # Checks if correct key solution was entered
    if answer == key :
        # correct answer
        print("Problem solved!")
        print("Great work!")
        score += 10
        successful_loops += 1
        if successful_loops >= 5:
            energy.current += 5
            print("5 or more successful events in a row! Here's 5 energy!")
        continue
    else:
        # incorrect answer
        energy.current -= current_event.dmg
        print("You entered an incorrect code or you ran out of time!")
        print("You have lost " + str(current_event.dmg) + " energy")
        score += 1
        successful_loops = 0
        continue