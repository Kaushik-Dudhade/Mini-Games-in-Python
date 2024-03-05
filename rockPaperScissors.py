import random

play = input("Do you want to play? ").lower()

if play != "yes":
    print("Okay Bye")
    quit()

user_score, computer_score = 0,0
print("Let's play !")

options = ["rock","paper","scissors"]

while True:
    player_choice = input("Enter rock/paper/scissors or Q to quit: ").lower()

    if player_choice == 'q':
        break

    if player_choice not in options:
        continue
    
    random_number = random.randint(0,2)
    comp_choice = options[random_number]

    print("Your Choice = ",player_choice)
    print("Computer choice = ", comp_choice)

    if player_choice == comp_choice:
        print("It's a Tie !")

    elif player_choice == "rock" and comp_choice == "scissors":
        print("You win !")
        user_score += 1
    
    elif player_choice == "paper" and comp_choice == "rock":
        print("You win !")
        user_score += 1

    elif player_choice == "scissors" and comp_choice == "paper":
        print("You win !")
        user_score += 1

    else:
        print("You lose !")
        computer_score += 1
    
print("Your score is", user_score, ".")
print("Computer score is", computer_score, ".")
print("Thanks For Playing !!")

quit()
