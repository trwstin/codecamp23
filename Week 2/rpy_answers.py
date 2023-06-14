import random

# Print multiline instruction
# performstring concatenation of string
print("Winning Rules of the Rock Paper Scissors game as follows: \n"
	+ "Rock vs Paper -> Paper wins \n"
	+ "Rock vs Scissors -> Rock wins \n"
	+ "Paper vs Scissors -> Scissors wins \n")

play = True

while play:
    print("Enter choice \n 1 for Rock, \n 2 for Paper, and \n 3 for Scissors \n")

	# take the input from player
    player_choice = int(input("Player turn: "))

    # If player choose 1 for "Rock"
    if player_choice == 1:
        player_choice_name = "Rock"
    # If player choose 2 for "Paper"
    elif player_choice == 2:
        player_choice_name = "Paper"
    # If player choose 3 for "Scissors"
    else:
        player_choice_name = "Scissors"

    # print player choice
    print("Player's choice is: " + player_choice_name)
    print("\nNow it's the computer's turn.......")

    # Computer makes a random choice or 1, 2 or 3
    comp_choice = random.randint(1, 3)

    # If Computer choose 1 for "Rock"
    if comp_choice == 1:
        comp_choice_name = "Rock"
    # If Computer choose 2 for "Paper"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    # If Computer choose 3 for "Scissors"
    else:
        comp_choice_name = "Scissors"

    # print comp choice
    print("Computer's choice is: " + comp_choice_name)

    # print vs
    print(player_choice_name + " V/S " + comp_choice_name)

    # Base case: Player loses, result = "Lose"
    result = "Lose"

    # If choices are the same, change result to "Draw"
    if player_choice == comp_choice:
        result = "Draw"

    # If the Player Wins, change result to "Win"
    elif player_choice_name == "Rock" and comp_choice_name == "Scissors":
        result = "Win"
    elif player_choice_name == "Paper" and comp_choice_name == "Rock":
        result = "Win"
    elif player_choice_name == "Scissors" and comp_choice_name == "Paper":
        result = "Win"

    # Printing the Result of the game
    if result == "Draw":
        print("<== It's a tie ==>")
    elif result == "Win":
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")

    # do you want to play again?
    print("Do you want to play again? (Y/N)")
    ans = input().lower()

    # if Player input n or N then change play to "False", to stop the While loop
    if ans == 'n':
        play = False

# after coming out of the while loop
# we print thanks for playing
print("\nThanks for Playing!")