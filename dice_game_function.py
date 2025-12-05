import random

from numpy import roll

def roll_dice():
    def_dice = random.randint(1, 6) + random.randint(1, 6)
    return def_dice

def main():
 print("welcome to the dice game!")
 player1 = input("enter player1 name:")
 player2 = input("enter player2 name:") 

 roll1 = roll_dice()
 roll2 = roll_dice()

 print(player1, 'rolled: ', roll1) 
 print(player2, 'rolled: ', roll2) 

 if roll1 > roll2:
     print(player1 + " wins!")
 elif roll2 > roll1:
     print(player2 + " wins!")
 else:
     print("It's a tie!")

main()