# Hangman (Simple Version)

import random

# Initialize

# Students can add their own words
words = ["CODECAMP", "PYTHON", "SINGAPORE", "COMPUTER", "LAPTOP", "CODING"]

word = random.choice(words)
guess = "-" * len(word)
wrong_letters = ""

# Print header
print("HANGMAN\n")

print("""
-------
|     
|    
|    
|    
|
|---------""")

# Main game loop
# How do you begin a while loop?
_____ ____:
    print(f"Current Guess: {guess}")
    print(f"Wrong Guesses: {wrong_letters}")
    
    # How do you get the user to enter an input?
    letter = _____("\nPlease enter a letter. > ").upper()
    
    # Check if the letter is in the word
    __ ______ in word:
        temp = ""
        ___ index in range(len(word)):
            __ letter == word[index]:
                temp += letter
            ____ guess[index] != "-": # How do you provide an alternate if statement?
                temp += guess[index]
            ____: # What must be present to close an if statement?
                temp += "-"
        guess = temp
                
    ____: # Challenge! What do you think should go here?
        wrong_letters += letter
        
        
    # Check for a winner, when the word is same as the guess
    __ ____ __ _____:
        print("You win!")
        print("""
     O
    \\|/
     |
    / \\""")
        exit()

    # Print the hangman
    # Use the correct method to count the number of wrong letters in wrong_letters

    if ___(wrong_letters) == 0:
        print("""
-------
|     
|    
|    
|    
|
|---------""")

    if ___(wrong_letters) == 1:
        print("""
-------
|     O
|    
|    
|    
|
|---------""")

    if ___(wrong_letters) == 2:
        print("""
-------
|     O
|     |
|     |
|    
|
|---------""")

    if ___(wrong_letters) == 3:
        print("""
-------
|     O
|    \\|/
|     |
|    
|
|---------""")

    if ___(wrong_letters) == 4:
        print("""
-------
|     O
|    \\|/
|     |
|    / \\
|
|---------""")
    
    if ___(wrong_letters) == 5:
        print("""
-------
|     |
|     O
|    /|\\
|     |
|    | |
|---------""")

    # Check for a loser
    if ___(wrong_letters) == 5:
        print("You lose!")
        print(f"The word was {word}")
        exit()
