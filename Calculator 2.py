print("Welcome to the budget calculator 2.0.")
x = input("Do you want to use the calculator?[yes/no] : ")
y = x.lower()

def addition(*a):
    return sum(a)

def subtraction(a,b):
    return a-b

import math
def multiplication(*a):
    return math.prod(a)

def division(a,b):
    return a/b

def leftover(a,b):
        return a%b

while True:
    if y == "no":
        print("Thanks, use me to calculate anything when you want.")
        break
    elif y != "yes" and y != "no":
        print("Invalid input. Please insert either yes or no.")
        break
    else:
        z = input("What do you want to do?[(+)(-)(*)(/)(%)] : ")
        i = 1
        if z == "+":
            num = []
            while True:
                num1 = input(f"Enter number {i} : ")
                i += 1
                if num1 == "=":
                 break
                num2 = float(num1)
                num.append(num2)
            print("The total is : ", addition(*num))
        elif z == "-":
            a = float(input(f"Enter number {i} : "))
            b = float(input(f"Enter number {i+1} : "))
            print("the subtraction is : " , subtraction(a,b))
        elif z == "*":
            num = []
            while True:
                num1 = input(f"Enter number {i} : ")
                i += 1
                if num1 == "=":
                 break
                num2 = float(num1)
                num.append(num2)
            print("The result is : ", multiplication(*num))
        elif z == "/":
            a = float(input(f"Enter number {i} : "))
            b = float(input(f"Enter number {i+1} : "))
            if b == 0:
                print("Error: Cannot devide by zero.")
            else:
                print("The result is : ", division(a,b))
        elif z == "%":
            a = float(input(f"Enter number {i} : "))
            b = float(input(f"Enter number {i+1} : "))
            if b == 0:
                print("Error: Cannot devide by zero.")
            else:
                print("The leftover is : ", leftover(a,b))
        else:
            print("Invalid input, please insert one of these [(+)(-)(*)(/)(%)] as input")
    ans = input("Do you want to use the calculator again?[yes/no] : ")
    answer = ans.lower()
    if answer == "no":
        print("Thank you for using this calculator. Hopefully, we will meet again.")
        break
    elif answer == "yes":
        continue
    else:
        print("Invalid input. Please insert either yes or no. Thank you.")
        break
