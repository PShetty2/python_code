import Game, Role1, Role2
print("Welcome to the game MapleStory! You are a chosen hero of Maple World.")
print("You have been given the mission of defeating the evil Black Mage in order to save Maple World from falling into ruin!")
print("\nGameplay rules: There are three challenges to complete. You will do these challenges by rolling two six-sided dice with a range of 2-12.")
print("The outcome of the challenges will be determined by the roll value(sum of the numbers rolled on the dice) + the attribute value related to the challenge.") 
print("Roll value + attribute will give different results(E.g. (6+1) + STR 2= 9. Challenge won, no change in attribute):")
print("""a.	Critical Loss (e.g., 2 - 4): challenge is lost and the attribute that is based on is decreased
b.	Loss (e.g., 5-8): challenge is lost, no change in the character’s attributes
c.	Win (e.g., 9-11): challenge is won, no change in the character’s attributes
d.	Critical Win (e.g., 12-14): challenge is won and the attribute that is based on increases
""")
print('You must win all three challenges to win the game.')
role = input("You must choose between two roles to fight as. Will you be a Buccaneer, or a Ice/Lightning mage?(Enter 1 or 2): ")
if role == 1:
    Game.Role1


print("Dear hero of Maple World! The Black Mage is threatening to destroy all of Maple World, and only you can stop him! In order to defeat him you must overcome three challenges.")
