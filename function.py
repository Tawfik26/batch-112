# def mama():
#     print("I am bossking")

# mama()

# def addition(a=10,b=4):  # a=10 & b=4 are default values
#     print(a+b)
# addition()
# addition(2,3)
# addition(2) # here a=2 & b=4(from default)
# addition(0,3) # here a=0 & b=3 (no default value)

# def addition(*a):
#     return sum(a)

# num=[]

# for i in range(3):
#     num1=float(input(f"Enter number {i+1} :"))
#     num.append(num1)

# result=addition(*num)
# print(result)

# def addition(*a):
#     # return sum(a)
#     print(sum(a))

# num=[]

# for i in range(3):
#     num1=float(input(f"Enter number {i+1} :"))
#     num.append(num1)

# # result=addition(*num)
# # print(result)
# addition(*num)

# def addition(*a):
#     print(sum(a))

# addition(23,22,56,89)

# x=(3,5,6)
# print(sum(x))

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*factorial(n-1) # function within function is called recartion
    
# a=int(input("Enter a number : "))
# result = factorial(a)
# print(f"The factorial of {a} is :", result)

# def addition(a):
#     # print(a+10)
#     return a+10
# # addition(23)
# result=addition(23)
# print(result)

# result=lambda a:a+10
# print(result(12))

# a=(12,34,[56,58,2]) # can add/remove anything from a list even if it is inside of a tuple

# print(a)
# print(a[2])
# a[2].append(3)
# a[2].remove(2)
# print(a)

# age = 17

# status = "Adult" if age >= 18 else "Minor"  # condition line if-else

# print(status)

# [print(i) for i in range(6)]

# a = [i for i in range(5)]
# print(a)

# def addition(*a):
#     return sum(a)

# num = []

# i = 0
# while True:
#     num1 = input(f"Enter number {i+1} : ")
#     i += 1
#     if num1 == "=":
#         break
#     num2 = float(num1)
#     num.append(num2)

# # print(num)
# print("The total is : ", addition(*num))

# import math

# def multiplication(*a):
#     return math.prod(a) 

# num = []

# i = 1
# while True:
#     num1 = float(input(f"Enter number {i} : "))
#     i += 1
#     num.append(num1)
#     if num1 == 1:
#      break
# print("The result is : ", multiplication(*num))

# import math
# def multiplication(*a):
#     multiply = math.prod(a)
#     print("The result is : ", multiply)

# num = []

# i = 1

# while True:
#     num1 = input(f"Enter number {i} : ")
#     i += 1
#     if num1 == "=":
#         break
#     num2 = float(num1)
#     num.append(num2)
# multiplication(*num)


# def addition(*a):
#     total = sum(a)
#     print(f"The total is : ", total)

# num = []

# i = 1

# while True:
#     num1 = input("Enter number {i} : ")
#     i += 1
#     if num1 == "=":
#         break
#     num2 = float(num1)
#     num.append(num2)

# addition(*num)


import math
def multiplication(*a):
    multiply = math.prod(a)
    print("The result is : ", multiply)

num = []

i = 1

while True:
    num1 = input(f"Enter number {i} : ")
    i += 1
    if num1 == "=":
        break
    num2 = float(num1)
    num.append(num2)
multiplication(*num)


