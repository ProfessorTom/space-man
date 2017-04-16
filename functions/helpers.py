from classes.events import Event
from classes.game import Energy

def playerIsDead(energy, score):
    if energy.current <= 0:
        print('\nGame Over! Your ship sustained too much damage.\n')
        energy.display()

        print("Your score is " + str(score))
        return True
        # running = False
        #time.sleep(5)
        #break #is this necessary?
    else:
        return False