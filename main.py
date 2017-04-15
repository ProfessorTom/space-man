import random
from classes.events import Event

print('Welcome to the game!')

energy = 100

# Defining Events
low_air = Event("Low Air", "ghA")
asteroid = Event("Asteroid", "aRu")
black_hole = Event("Black hole", "Oyn")

event_list = [low_air, asteroid, black_hole]

while energy > 0:

    print('Current energy level is ' + str(energy) + '%')

    chance = random.randint(0, 2)

    event_list[chance].show()

    if energy <= 0:

        print('Game Over! Your ship sustained too much damage.')

    break