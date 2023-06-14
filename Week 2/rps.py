import random

# Replace the Blanks(underscores) with the answers

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

    # If player choose 1
    if player_choice == 1:
        player_choice_name = "Rock"
    # If player choose 2
    elif player_choice == 2:
        player_choice_name = "_____"
    # If player choose 3
    else:
        player_choice_name = "________"

    # print player choice
    print("Player's choice is: " + player_choice_name)
    print("\nNow it's the computer's turn.......")

    # Computer makes a random choice or 1, 2 or 3
    comp_choice = random.randint(1, 3)

    # If Computer choose 1
    if comp_choice == 1:
        comp_choice_name = "____"
    # If Computer choose 2
    elif comp_choice == 2:
        comp_choice_name = "_____"
    # If Computer choose 3
    else:
        comp_choice_name = "________"

    # print computer's choice
    print("Computer's choice is: " + ________________)

    # print player's choice vs computer's choice
    print(player_choice_name + " V/S " + ________________)

    # Base case: Player loses, result = "Lose"
    result = "Lose"

    # If choices are the same, change result to "Draw"
    if player_choice == comp_choice:
        result = "____"

    # If the Player Wins
    elif player_choice_name == "Rock" and comp_choice_name == "Scissors":
        result = "___"
    elif player_choice_name == "Paper" and comp_choice_name == "____":
        result = "___"
    elif player_choice_name == "________" and comp_choice_name == "Paper":
        result = "___"

    # Printing the Result of the game
    if result == "____":
        print("<== It's a tie ==>")
    elif result == "___":
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")

    # do you want to play again?
    print("Do you want to play again? (Y/N)")
    ans = input().lower()

    # if Player input n or N then change play to "False", to stop the While loop
    if ans == 'n':
        play = _____

# after coming out of the while loop
# we print thanks for playing
print("\nThanks for Playing!")