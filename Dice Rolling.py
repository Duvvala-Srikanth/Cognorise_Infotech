import random
def dice_game():
    while True:
        no_of_sides=int(input("Enter the number of sides on dice:"))
        no_of_rolls=int(input("Enter the number of rolls of dice:"))
        if no_of_sides<=0 or no_of_rolls<=0:
            print("Enter positive number")
        else:
            break
    for i in range(1,no_of_rolls+1):
        dice_result=random.randint(1,no_of_sides)
        print("The dice result is:",dice_result)
    while True:
        play_again = input("Do you want to play again?  (yes/no):").lower()
        if play_again=='yes':
            return dice_game()
        else:
            break
dice_game()
print('the game is over!')