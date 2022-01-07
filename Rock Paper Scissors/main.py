from random import randint

options = ['rock','scissors','paper']
computer_choice = options[randint(0, (options.__len__() - 1))]
user_choice = input("Choose from 'rock', 'paper', 'scissors'.\nType your choice and then press enter: ")
user_choice = user_choice.lower()

if(computer_choice == options[0]):
    if(user_choice == options[1]):
        results = "Rock beats scissors\nComputer won!"
    elif(user_choice == options[2]):
        results = "Paper covers rock\nUser won!"
    elif(user_choice == options[0]):
        results = "Its a draw"
elif(computer_choice == options[1]):
    if(user_choice == options[0]):
        results = "Rock beats scissors\nUser won!"
    elif(user_choice == options[1]):
        results = "Its a draw"
    elif(user_choice == options[2]):
        results = "Scissors cuts paper\nComputer won!"
elif(computer_choice == options[2]):
    if(user_choice == options[0]):
        results = "Paper covers rock\nComputer won!"
    elif(user_choice == options[1]):
        results = "Scissors cuts paper\nUser won!"
    elif(user_choice == options[2]):
        results = "Its a draw"

print(f"\nComputer chose: {computer_choice}")
print(f"User chose: {user_choice}")
print("\n"+results)