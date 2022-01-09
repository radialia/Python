# Importing all the required modules
from words import word_list
from random import randint

# ASCII art for the levels
levels = [
    """
    _______
     |/
     |
     |
     |
     |
     |
    _|___
    """,
    """
    _______
     |/      |
     |
     |
     |
     |
     |
    _|___
    """,
    """
    _______
     |/      |
     |      (_)
     |
     |
     |
     |
    _|___
    """,
    """
    _______
     |/      |
     |      (_)
     |       |
     |
     |
     |
    _|___
    """,
    """
    _______
     |/      |
     |      (_)
     |      \|
     |
     |
     |
    _|___
    """,
    """
    _______
     |/      |
     |      (_)
     |      \|/
     |
     |
     |
    _|___
    """,
    """
    _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |
     |
    _|___
    """,
    """
    _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      /
     |
    _|___
    """,
    """
    _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___
    """,
]

# Welcome menu
def display():
    print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
        """)
    print("Hello!! Welcome to the hangman game!")
    print(levels[0])
    print("You need to guess the word before the man is hanged!\nWith every wrong guess the man progresses to be hanged!\nGuesses you got: 8\n\nBEST OF LUCK!\n")



def difficulty():
    print("\nSelect a difficulty\n")
    level = int(input("Enter the number of your difficulty:\n1.Easy\n2.Intermediate\n3.Hard\n>>> "))
    print("\n")
    easy_difficulty = []
    intermediate_difficulty = []
    hard_difficulty = []
    for words in word_list:
        if(level == 1):
            if(words.__len__() <= 5):
                easy_difficulty.append(words)
        elif(level == 2):
            if(words.__len__() <= 7):
                intermediate_difficulty.append(words)
        else:
            hard_difficulty.append(words)

    if(level == 1):
        return easy_difficulty
    elif(level == 2):
        return intermediate_difficulty
    else:
        return hard_difficulty



def level_executer(array):
    word = array[randint(0, (len(array) - 1))]
    return word


# Functionality of the Game
def game():
    display()

    word = level_executer(difficulty())
    guesses = 0
    guessed = False
    guess_display = []

    for letters in word:
        guess_display.append("_ ")

    while not guessed:
        print(f" ".join(guess_display))
        guess = input("\nEnter your guess: ")

        if("_" in f" ".join(guess_display)):
            if(guess in word):
                guess_display[word.index(guess)] = guess
            elif(guess not in word):
                print(f"\nThere is no {guess} in the word! You lose a life")
                guesses += 1
                print(f"You have {8-guesses} left")
                print(levels[guesses])
                if(guesses == int(levels.__len__() - 1)):
                    print(f"\nYou have exhausted all of your lifelines! The word was {word}. The man is hanged! Game Over!")
                    guessed = True
                
        elif("_" not in f" ".join(guess_display)):
            print(f"You have guessed the word in {guesses}")
            guessed = True

if __name__ == '__main__':
    game()