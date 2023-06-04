import random

# Print multiline instruction
# performstring concatenation of string
print("Winning Rules of the Rock paper scissor game as follows: \n"
	+ "Rock vs paper->paper wins \n"
	+ "Rock vs scissor->Rock wins \n"
	+ "paper vs scissor->scissor wins \n")

play = True

while play:
    print("Enter choice \n 1 for Rock, \n 2 for paper, and \n 3 for scissor \n")

	# take the input from user
    choice = int(input("User turn: "))

    if choice == 1:
        user_choice_name = "Rock"
    elif choice == 2:
        user_choice_name = "Paper"
    else:
        user_choice_name = "Scissor"

    # print user choice
    print("user choice is: " + user_choice_name)
    print("\nNow its computer turn.......")

    # comp choice
    comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissor"

    # print comp choice
    print("Computer choice is: " + comp_choice_name)

    # print vs
    print(user_choice_name + " V/s " + comp_choice_name)

    result = "Lose"
    if choice == comp_choice:
        result = "Draw"
    elif user_choice_name == "Rock" and comp_choice_name == "Scissor":
        result = "Win"
    elif user_choice_name == "Paper" and comp_choice_name == "Rock":
        result = "Win"
    elif user_choice_name == "Scissor" and comp_choice_name == "Paper":
        result = "Win"

    # Printing either user or computer wins or draw
    if result == "Draw":
        print("<== Its a tie ==>")
    elif result == "Win":
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")

    # do you want to play again?
    print("Do you want to play again? (Y/N)")
    ans = input().lower

    # if user input n or N then condition is True
    if ans == 'n':
        play = False

# after coming out of the while loop
# we print thanks for playing
print("\nThanks for playing")