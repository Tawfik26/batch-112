print("Welcome to calculator pro (budget verson)")
x = input("Do you want to use the calculator?[yes/no] : ")
y = x.lower()

def addition(*a):
    total = sum(a)
    print("The total is : ", total)

def subtraction(a,b):
    subtraction = a-b
    print("The subtraction is : " , subtraction)

import math
def multiplication(*a):
    multiply = math.prod(a)
    print("The result is : ", multiply)

def division(a,b):
    if b == 0:
        print("Error: Cannot devide by zero.")
    else:
        divi = a/b
        print("The result is : ", divi)

def leftover(a,b):
    if b == 0:
        print("Error: Cannot devide by zero.")
    else:
        left = a%b
        print("The leftover is : ", left)

while True:
    if y == "no":
        print("Thanks, use this to calculate anything when you want.")
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
                print("Enter = (equal sign) to get the total.")
                num1 = input(f"Enter number {i} : ")
                i += 1
                if num1 == "=":
                 break
                num2 = float(num1)
                num.append(num2)
            addition(*num)
        elif z == "-":
            a = float(input(f"Enter number {i} : "))
            b = float(input(f"Enter number {i+1} : "))
            subtraction(a,b)
        elif z == "*":
            num = []
            while True:
                print("Enter = (equal sign) to get the result.")
                num1 = input(f"Enter number {i} : ")
                i += 1
                if num1 == "=":
                 break
                num2 = float(num1)
                num.append(num2)
            multiplication(*num)
        elif z == "/":
            a = float(input(f"Enter number {i} : "))
            b = float(input(f"Enter number {i+1} : "))
            division(a,b)
        elif z == "%":
            a = float(input(f"Enter number {i} : "))
            b = float(input(f"Enter number {i+1} : "))
            leftover(a,b)
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
