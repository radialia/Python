from random import randint

def Game():
    print("""
                                    __   __                                     __               
.-----.--.--.-----.-----.-----.    |  |_|  |--.-----.    .-----.--.--.--------.|  |--.-----.----.
|  _  |  |  |  -__|__ --|__ --|    |   _|     |  -__|    |     |  |  |        ||  _  |  -__|   _|
|___  |_____|_____|_____|_____|    |____|__|__|_____|    |__|__|_____|__|__|__||_____|_____|__|  
|_____|                                                                                          

        """)
    print("Welcome to Guess the Number\nGuess the number that the computer is thinking within limited guesses!\n\nBEST OF LUCK")

    number = randint(0,100)
    tries = 10

    while tries > 0:
        guess = int(input("\n\nEnter your guess\n>>> "))

        if(guess < number):
            tries -= 1
            print(f"Your guess is lower than the original number\nRemaining tries: {tries}")
        elif(guess > number):
            tries -= 1
            print(f"Your guess is higher than the original number\nRemaining tries: {tries}")
        else:
            print("You got the number!\nCongratulations!")
            break

Game()
