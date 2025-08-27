print("Welcome to memorized calculator. Where you can use your previous result.")

def addition(*a):
    return sum(a)

def subtraction(a, b):
    return a - b

import math
def multiplication(*a):
    return math.prod(a)

def division(a, b):
    if b == 0:
        print("Error: Cannot divide by zero.")
        return None, None
    else:
        div = a / b
        left = a % b
        return div, left

def invalid():
    print("Invalid input, only numbers can be taken as input here. Please insert numbers here. Thank you.")

running = True
r = None   # to store previous result

while running:
    while True:
        z = input("What do you want to do?[(+)(-)(*)(/)] : ")
        if z in ["+","-","*","/"]:
            break
        else:
            print("Invalid input, please insert one of these [(+)(-)(*)(/)] as input. Thank you")

    i = 1
    num = []

    if z in ["+","*"]:
        while True:
            if r is not None:
                print(f"(Previous result : {r})\nInsert r to use that. Thank you.")
            print("Enter = (equal sign) to get the result.")
            num1 = input(f"Enter number {i} : ")
            if num1 == "=":
                break
            if r is not None and num1.lower() == "r":
                num2 = r
                print(f"Using previous result: {r}")
            else:
                try:
                    num2 = float(num1)
                except ValueError:
                    invalid()
                    continue
            num.append(num2)
            i += 1

        if z == "+":
            r = addition(*num)
            print(f"Sum of those {i-1} numbers is: {r}")
        elif z == "*":
            r = multiplication(*num)
            print(f"Multiplication of those {i-1} numbers is: {r}")

    elif z in ["-","/"]:
        while True:
            if r is not None:
                print(f"(Previous result : {r})\nInsert r to use that. Thank you.")
            num1 = input(f"Enter number {i} : ")
            if r is not None and num1.lower() == "r":
                a = r
                print(f"Using previous result: {r}")
                break
            try:
                a = float(num1)
                break
            except ValueError:
                invalid()
                continue

        while True:
            if r is not None:
                print(f"(Previous result = {r})\nInsert r to use that. Thank you.")
            num2 = input(f"Enter number {i+1} : ")
            if r is not None and num2.lower() == "r":
                b = r
                print(f"Using previous result: {r}")
                break
            try:
                b = float(num2)
                break
            except ValueError:
                invalid()
                continue

        if z == "-":
            r = subtraction(a, b)
            print(f"The subtraction result of {a} - {b} is : {r}")
        elif z == "/":
            div, left = division(a, b)
            print(f"Result of {a} divided by {b} :\nDivision : {div}\nLeftover : {left}")

    while True:
        ans = input("Do you want to use the calculator again? [yes/no] : ").lower()
        if ans == "no":
            print("Thank you for using this calculator. Wish you good luck.")
            running = False
            break
        elif ans == "yes":
            break
        else:
            print("Invalid input. Please insert either yes or no. Thank you.")
            continue
