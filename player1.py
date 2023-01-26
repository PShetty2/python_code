import random
class player1:
    def show(self):
        name = "player 1"
        print(name)
        diceThrow = random.randrange(1, 7)       # return an int, one of 1,2,3,4,5,6
        diceThrow2 = random.randrange(1, 7) 
        diceThrow3 = random.randrange(1, 7) 
        print(diceThrow, diceThrow2, diceThrow3)