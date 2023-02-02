import random
Strength = 2
Intelligence = 1
Luck = 1
def rollme():
    dice1 = random.randrange(1, 7) #returns a value from 1 to 6
    dice2 = random.randrange(1,7)
    roll_value = dice1 + dice2
    global Strength
    print("roll_value", roll_value)
    total_value = roll_value + Strength
    print("total_value",total_value)
    if total_value <= 4:
        print("Challenge is lost. Strength attribute is decreased.")
        Strength -= 1
    elif total_value >= 5 or total_value <= 8:
        print("Challenge is lost.")
    elif total_value >= 9 or total_value <= 11:
        print("Challenge is won!")
    elif total_value >= 12 or total_value <= 14:
        print("Challenge is won! Strength attribute is increased.")
        Strength += 1

def challenge1():
    print("You must defeat two of the Black Mage's followers before you can face him! First you must defeat the Balrog!") 
    print("Use your strength(STR) to brute force your way through it.")

    