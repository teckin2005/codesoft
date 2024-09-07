print('''
      

░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝
''')

import random

def get_computer_choice():
    return random.randint(1, 3)

def get_user_choice():
    valid_input = ("1", "2", "3")
    while True:
        user_input = input("Enter 1: FOR ROCK\nEnter 2: FOR PAPER\nEnter 3: FOR SCISSORS\n- ")
        if user_input in valid_input:
            return int(user_input)
        else:
            print("Invalid Input. Try Again.")
            print("   ")

def print_choice(choice, player):
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(f".....{player} chose {choices[choice]}.....")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "user"
    else:
        return "computer"

def play_game():
    max_points = int(input("ENTER MAXIMUM NUMBER OF POINTS:"))
    user_score, computer_score = 0, 0

    while user_score < max_points and computer_score < max_points:
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()

        print_choice(computer_choice, "Computer")
        print_choice(user_choice, "You")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "tie":
            print("<<<TIE>>>")
        elif winner == "user":
            print("***YOU WIN***")
            user_score += 1
        else:
            print("###YOU LOST###")
            computer_score += 1

        print(f"Current Score -> You: {user_score}, Computer: {computer_score}")

    if user_score == max_points:
        print("<<<<<<<<< HURRAY! YOU WON THE GAME >>>>>>>>>>>")
    else:
        print("???? YOU LOST THE GAME ????")

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()