"""
rock smashes scissors
scissors cuts paper
paper covers rock

"""

"""
pseudocode

store the list of possible choices
get user input 
get the computer guess

compare who won

ask the user to play again

"""

# store the list of possible choices
import random
# computer, user
scores = [0,0]
player_name = input(" what is your name ? \n")
while True:
    choices = ["rock", "scissors", "paper"]

    user_input  = input("Please enter your choice. Choices are" + str(choices)+ "\n")

    print("you selected "+user_input)

    if user_input not in choices: 
        print(user_input + " is not a valid choice")
    else:
        computer_choice = random.choice(choices)
        print("computer chose " + computer_choice)

    
    if user_input == computer_choice:
        # update computer marks
        scores[0]+= 0.5
        # update user marks
        scores[1]+= 0.5
        print("A Draw !")
    elif user_input == "rock" and computer_choice== "scissors":
        scores[1]+= 1
        print("You won!")
    elif user_input == "paper" and computer_choice== "rock":
        scores[1]+= 1
        print("You Won!")
    elif user_input == "scissors" and computer_choice== "paper":
        scores[1]+= 1
        print("You Won!")
    elif computer_choice == "rock" and user_input== "scissors":
        scores[0]+= 1
        print("You lost!")
    elif computer_choice == "paper" and user_input== "rock":
        scores[0]+= 1
        print("You lost!")
    else:
        scores[0]+= 1
        print("You lost!")

    play_again = input("Do you want to play again? (y/n): ")

    if play_again == "y":
        print("\n")
    else:
        print("Good Bye")
        print("Here are the scores")
        print("--------------------------------")
        print("COMPUTER |  "+player_name )
        print("--------------------------------")
        print(str(scores[0])+"      | "+ str(scores[1]))
        break




