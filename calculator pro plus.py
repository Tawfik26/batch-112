
print("Welcome to calculator pro. (budget version)")
while True:
    x = input("Do you want to use the calculator?[yes/no] : ")
    y = x.lower()
    if y == "no":
        print("Ok, use this calculator to calculate anything. Wish you a nice day.")
        running = False     #or could use exit(), just that would exit out of the entire program.
        break
    elif y == "yes":
        running = True
        break
    else:
       print("Invalid input. Please insert either yes or no.") 

def addition(*a):
    return sum(a)

def subtraction(a,b):
    subtraction = a-b
    print(f"The subtraction result of {a} to {b} is : " , subtraction)


import math
def multiplication(*a):
    multiply = math.prod(a)
    return multiply

def division(a,b):
    if b == 0:
        print("Error: Cannot divide by zero.")
    else:
        divi = a/b
        print(f"Result of {a} divided by {b} is : ", divi)

def leftover(a,b):
    if b == 0:
        print("Error: Cannot divide by zero.")
    else:
        left = a%b
        print(f"The leftover of {a} divided by {b} is : ", left)

def invalid():
    print("Invalid input, only numbers can be taken as input here. Thank you.")

while running:
    while True:
        z = input("What do you want to do?[(+)(-)(*)(/)(%)] : ")
        if z in ["+","-","*","/","%"]:
            break
        else:
            print("Invalid input, please insert one of these [(+)(-)(*)(/)(%)] as input. Thank you")
    i = 1
    num = []
    if z == "+":
        while True:
            print("Enter = (equal sign) to get the total.")
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
        print(f"Sum of those {i-1} numbers is: ", addition(*num))
    elif z == "-":
        while True:
            try:
                a = float(input(f"Enter number {i} : "))
                # b = float(input(f"Enter number {i+1} : "))
                # subtraction(a,b)
                break
            except ValueError:
                invalid()
        while True:
            try:
                # a = float(input(f"Enter number {i} : "))
                b = float(input(f"Enter number {i+1} : "))
                # subtraction(a,b)
                break
            except ValueError:
                invalid()
        
        subtraction(a,b)

    elif z == "*":
        while True:
            print("Enter = (equal sign) to get the result.")
            num1 = input(f"Enter number {i} : ")

            if num1 == "=":
                break
            try:
                num2 = float(num1)
                num.append(num2)
                i += 1
            except ValueError:
                invalid()
                continue
            
        print(f"Mutiplication of those {i-1} numbers is : ", multiplication(*num))
    elif z == "/":
        while True:
            try:
                a = float(input(f"Enter number {i} : "))
                # b = float(input(f"Enter number {i+1} : "))
                # division(a,b)
                break
            except ValueError:
                invalid()
                continue
        while True:
            try:
                # a = float(input(f"Enter number {i} : "))
                b = float(input(f"Enter number {i+1} : "))
                break
            except ValueError:
                invalid()
                continue
        
        division(a,b)

    elif z == "%":
        while True:
            try:
                a = float(input(f"Enter number {i} : "))
                # b = float(input(f"Enter number {i+1} : "))
                # leftover(a,b)
                break
            except ValueError:
                invalid()
                continue
        while True:
            try:
                # a = float(input(f"Enter number {i} : "))
                b = float(input(f"Enter number {i+1} : "))
                break
            except ValueError:
                invalid()
                continue
        
        leftover(a,b)

    while True:
        ans = input("Do you want to use the calculator again?[yes/no] : ")
        answer = ans.lower()
        if answer == "no":
            print("Thank you for using this calculator. Wish you good luck.")
            running = False
            break
        elif answer == "yes":
            break
        else:
            print("Invalid input. Please insert either yes or no. Thank you.")
            continue
