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


def display():
    """
    This function is responsible for the printing of the ASCII art and welcome message on the screen
    """
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
    print(
        f"Hello!! Welcome to the hangman game!\n{levels[0]}\nYou need to guess the word before the man is hanged!\nWith every wrong guess the man progresses to be hanged!\nGuesses you got: 8\n\nBEST OF LUCK!\n")


def difficulty():
    """
    This function is responsible for getting the level as user input and appending the words according to their lengths in the respective arrays.
    :return = Array of difficulty
    """
    easy_difficulty = []
    intermediate_difficulty = []
    hard_difficulty = []

    print("\nSelect a difficulty\n")
    level = int(input(
        "Enter the number of your difficulty:\n1.Easy\n2.Intermediate\n3.Hard\n>>> "))

    for words in word_list:
        if(words.__len__() <= 5):
            easy_difficulty.append(words)
        elif(words.__len__() <= 7):
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
    """
    This function is responsible for getting a random word from the returned array
    :param = array of words chosen according to difficulty
    :return = the random chosen word from the array of words passed as a paramater
    """
    word = array[randint(0, (len(array) - 1))]
    return word


def game():
    """
    This function is responsible for the the logic of the game
    """
    display()

    word = level_executer(difficulty())
    guesses = 0
    guessed = False
    guess_display = []

    for _ in word:
        guess_display.append("_ ")

    while not guessed:
        print(f" ".join(guess_display))
        guess = input("\nEnter your guess: ").lower()

        if guess in guess_display:
            print(f"You've already guessed {guess}")

        for position in range(word.__len__()):
            letter = word[position]
            if letter == guess:
                guess_display[position] = guess

        if(guess not in word):
            print(f"\nThere is no {guess} in the word! You lose a life")
            guesses += 1
            print(f"You have {8-guesses} left")
            print(levels[guesses])
            if(guesses == int(levels.__len__() - 1)):
                print(
                    f"\nYou have exhausted all of your lifelines! The word was {word}. The man is hanged! Game Over!")
                guessed = True

        if("_" not in f" ".join(guess_display)):
            print(f"You have guessed the word!")
            guessed = True


if __name__ == '__main__':
    game()
