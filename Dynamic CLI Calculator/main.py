def Addition(a, b):
    print(f"{a} + {b} = {a + b}")
    return a+b


def Substraction(a, b):
    print(f"{a} - {b} = {a - b}")
    return a-b


def Multiplication(a, b):
    print(f"{a} * {b} = {a * b}")
    return a*b


def Division(a, b):
    print(f"{a} / {b} = {a / b}")
    return a/b


def Modulus(a, b):
    print(f"{a} % {b} = {a % b}")
    return a % b


def Calculate(a, b, operator):
    if(operator == '+'):
        result = Addition(a, b)
    elif(operator == '-'):
        result = Substraction(a, b)
    elif(operator == '*'):
        result = Multiplication(a, b)
    elif(operator == '/'):
        result = Division(a, b)
    else:
        result = Modulus(a, b)

    return result


def App():
    print("""
 _____________________
|  _________________  |
| | @radialia    0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|\nGreetings! Welcome to Dynamic CLI Calculator\n\n
    """)
    a = int(input("Enter the first number: "))

    while True:
        operator = input("Enter the operator: ")
        b = int(input("Enter the second number: "))

        result = Calculate(a, b, operator)

        confirmation = input(
            f"Do wanna continue operation with {result}? (y/n)").lower()
        if(confirmation == 'y'):
            a = result
        else:
            break


App()
