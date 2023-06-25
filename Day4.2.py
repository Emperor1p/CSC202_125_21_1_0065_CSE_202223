
#ROCK-PAPER_SCISSORS
import random

game_images = ['Rock', 'Paper', 'Scissors']
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\nYou choose: "))
print(game_images[user_choice])
#2 will beat 1, 1 will beat 0 and 0 will 2
computer_choice = random.randint(0,2)
print(f"Computer choose {computer_choice}")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("User wins!, Rock beats Scissors")
elif computer_choice == 0  and user_choice == 2:
    print("You lose, Rock will beat Scissors")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif computer_choice ==  user_choice:
    print("It is draw")
elif user_choice == 1 and computer_choice == 2:
    print("You lose!, Scissors will beat Paper.")
elif user_choice == 2 and computer_choice == 1:
    print("You win!, Scissors beats Paper.")
elif user_choice == 0 and computer_choice == 1:
    print("You lose!, Paper will beat Rock.")
elif user_choice == 1 and computer_choice == 0:
    print("You win!, Paper beat Rock.")

  


