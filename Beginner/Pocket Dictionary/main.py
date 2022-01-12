from dictionary import dictionary
import os

while True:
    os.system('cls')
    print("Welcome to Pocket Dictionary!\nSearch for a word and get its meaning!\n\n")
    search = input("Enter your search\n>>> ").lower()
    if(search in dictionary):
        print(f"Meaning: {dictionary[search]}")
    else:
        print("Sorry! Word not found!!")

    flow = input("\nSearch for a word again? (y/n)\n>>> ").lower()
    if(flow == "y"):
        continue
    else:
        break