import random

# Computer comes up with a Number to guess
num = random.randint(1, 100)
chances = 0

# Player has 5 chances to guess
while chances <= 5:

  # Player guesses
  guess = int(input("Guess the number between 1 and 100! \n"))
  
  # If Player guesses the Number, Player wins the game
  if guess == num:
    print("That's correct! The number is " + str(num) + "!")
    print("Thanks for playing!")
    break

  # If Player's Guess is lower than the Number
  elif guess < num:
    print("That's incorrect! The number is more than " + str(guess) + "!")
    print("You have " + str((5 - chances)) + " tries left!")
    chances = chances + 1

  # If Player's Guess is higher than the Number
  elif guess > num:
    print("That's incorrect! The number is less than " + str(guess) + "!")
    print("You have " + str((5 - chances)) + " tries left!")
    chances = chances + 1

# Player has run out of Guesses
print("You have run out of Guesses!")
print("Thanks for playing!")
