import random

print("Welcome to Password Generator! Follow the instructions to create a strong password for yourself.")

letters = int(input("Enter the number of letters youwant in your password: "))
numbers = int(input("Enter the number of numbers you want in yoour password: "))
characters = int(input("Enter the number of characters you want in yoour password: "))

password_array = []
password = ""

letter_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number_list = ['1','2','3','4','5','6','7','8','9','0']
characters_list = ['!','@','#',"$",'%','^','&',"*",'(',')']

for char in range(0, letters):
    password_array.append(random.choice(letter_list))

for num in range(0, numbers):
    password_array.append(random.choice(number_list))

for specialChar in range(0, characters):
    password_array.append(random.choice(characters_list))

random.shuffle(password_array)
for passLetters in password_array:
    password += passLetters

print(password)