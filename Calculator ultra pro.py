
# Under construction# Under construction# Under construction# Under construction
# Under construction# Under construction# Under construction
# Under construction# Under construction
# Under construction

print("Welcome to calculator ultra. (budget version)")

def addition(*a):
    r = sum(a)
    return r

def subtraction(a,b):
    r = a-b
    print(f"The subtraction result of {a} to {b} is :  {r}")
    return r

import math
def multiplication(*a):
    r = math.prod(a)
    return r

def division(a,b):
    if b == 0:
        print("Error: Cannot divide by zero.")
    else:
        r = a/b
        rr = a%b
        print(f"Result of {a} divided by {b} :\nDivision :  {r}\nLeftover :  {rr}")
        return r

def invalid():
    print("Invalid input, only numbers can be taken as input here. Please insert numbers here. Thank you.")

running = True
while running:
    while True:
        z = input("What do you want to do?[(+)(-)(*)(/)] : ")
        if z in ["+","-","*","/"]:
            break
        else:
            print("Invalid input, please insert one of these [(+)(-)(*)(/)] as input. Thank you")
    i = 1
    num = []
    again = False
    while again:
            print(f"The previous result was {r}, insert that to use it. Thank you.")
    if z in ["+","*"]:
        while True:
            print("Enter = (equal sign) to get the result.")
            num1 = input(f"Enter number {i} : ")
            if num1 == "=":
                break
            try:
                num2 = float(num1)
                i += 1
            except ValueError:
                invalid()
                continue
            num.append(num2)
        if z == "+":
            r = addition(*num)
            print(f"Sum of those {i-1} numbers is: ", r)
        elif z == "*":
            r = multiplication(*num)
            print(f"Mutiplication of those {i-1} numbers is : ", r)
    elif z in ["-","/"]:
        while True:
            try:
                a = float(input(f"Enter number {i} : "))
                break
            except ValueError:
                invalid()
                continue
        while True:
            try:
                b = float(input(f"Enter number {i+1} : "))
                break
            except ValueError:
                invalid()
                continue
        if z == "-":
            subtraction(a,b)
        elif z == "/":
            division(a,b)

    while True:
        ans = input("Do you want to use the calculator again?[yes/no] : ")
        answer = ans.lower()
        if answer == "no":
            print("Thank you for using this calculator. Wish you good luck.")
            running = False
            break
        elif answer == "yes":
            answer = input(f"Do you want to use the previous result ({r})?[yes/no] : ").lower()
            if answer == "no":
                running = False
                break
            elif answer == "yes":
                running = True
                break
            else:
                print("Invalid input. Please insert either yes or no. Thank you.")
                continue
        else:
            print("Invalid input. Please insert either yes or no. Thank you.")
            continue
