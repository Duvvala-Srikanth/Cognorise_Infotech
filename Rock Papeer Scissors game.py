import random
print("Welcome to Rock, Paper, Scissors game")
user_score = 0
computer_score = 0
while True:
    user_choice = input("Enter your choice rock/scissor/paper:")
    if user_choice in ["rock", "paper", "scissor"]: 
        computer_choice = random.choice(['rock', 'paper', 'scissor'])  
        print(f"Computer choose: {computer_choice}")
        if user_choice == computer_choice:
            print("It is a tie")
        elif (user_choice=='rock' and computer_choice=='scissor'):
            print("Rock beats scissor\nYou win")
            user_score += 1
        elif (user_choice=='paper' and computer_choice=='rock'):
            print("Paper beats rock\nYou win")
            user_score += 1
        elif (user_choice=='scissor' and computer_choice=='paper'):
            print("Scissor beats paper\nYou win")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1
        print(f"Your score: {user_score}, Computer score: {computer_score}")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again!= 'yes':
        break
print("Thanks for playing!")