# print("Alu mama") # this is our first line code.

# # if 10>20:
# #     print(True)
# # else:
# #     print(False)

# a=10
# print(a+30)

# b="Murgi MamA aLu"
# # print(b[2:13])
# print(b)
# # print(b.upper())
# # print(b.lower())
# # print(b.capitalize())
# # print(b.title())
# # print(len(b))
# # print(b.index("L"))
# # print(b.find("A"))
# # print(b.replace("aLu","chacha"))
# print(b)
# # print(b.count("M"))
# print(b.swapcase())
# print(b.split())
# # print(b.strip())
# d=b.center(90,".")
# print(d)
# print(len(d))

# x=input("enter your name :")
# y=input("enter your age :")
# z=input("what are you learning:")

# # p="My name is {}, I am {} years old and I am learning {}"
# # print(p.format(x,y,z))
# print(f"My name is {x}, I am {y} years old, I am learning {z}")

# s="It's alright, \"he says.\""
# print(s)

# a=10
# b=100
# # print(a==b)
# print(a is not b)

# x="I am in Bangladesh"
# print("Bangladesh" not in x)

# print(7 & 3)    #Bitwise Operator   #7 = 0 1 1 1
                                    #3 = 0 0 1 1
                                    #------------
                                    #3 = 0 0 1 1 #Output is 3

# a=10
# b=22
# if a==b:
#     print("They are equal and the total is:",a+b)
# elif a>b:
#     print("a is bigger than b and the difference is",a-b) # print(f"a>b where the difference is {a-b}")
# elif a<b:
#     print("a is smaller than b and the difference is",b-a)
# else:
#     print("a and b are not equal")
# if a is b:  # is and  == are the same
#     if a==10:
#         print(a+b)
#     else:
#         print("a is not 10")
# elif a<b:
#     if a==11:
#         print(f"b is greater than a by: {b-a}")
#     else:
#         print("a is not equal to 11")
# else:
#     print("No match found")


# marks=int(input("Enter the marks:"))

# if marks<=100 and marks>0:
#     if marks>=80:
#         print("A+")
#     elif marks>=70:
#         print("A")
#     elif marks>=60:
#         print("A-")
#     else:
#         print("Fail")
# else:
#     print("Invalid input")


# import practice

# print(practice.a)

# import function as Mama
# print(Mama.a)

# import datetime

# a = datetime.datetime.now()

# print(a.time())
# print(a.date())
# print(a.strftime("%A"))
# print(a.strftime("%a"))
# print(a.strftime("%d"))
# print(a.strftime("%B"))     #upper case letter for full form and lower case letters for short form.
# print(a.strftime("%Y"))
# print(a.strftime("%X"))     #X for time and x for date.
# print(a.strftime("%x"))
# print(a.strftime("%c"))

# import os

# os.mkdir('ABCD')      #mkdir for create a file and rmdir for delete that file.
# os.rmdir('ABCD')

# a = os.listdir('.')     #all the files in that folder.
# print(a)

# os.rename("alu.txt","alu_mama.txt")

# import turtle

# screen = turtle.Screen()

# t = turtle.Turtle()

# for _ in range(4):
#     t.forward(100)
#     t.right(90)

# screen.mainloop()

# t.circle(100)

# screen.mainloop()

# import mamahama.main_2
# # from mamahama import main_2

# x = mamahama.main_2.b

# print(x)

# t = turtle.Turtle()

# t.hideturtle()

# t.penup()
# t.goto(0,0)
# t.color('red')
# t.write('Hello, Turtle!', align='center', font=("Gotham", 24,'bold'))

# turtle.done()

# t.penup()
# t.goto(-100,100)
# t.pendown()
# t.goto(100,-100)
# turtle.done()

# import turtle

# t = turtle.Turtle()

# t.penup()
# t.goto(-180,130)
# t.pendown()
# t.circle(100)

# t.penup()
# t.goto(40,130)
# t.pendown()
# t.circle(100)

# t.penup()
# t.goto(260,130)
# t.pendown()
# t.circle(100)

# t.penup()
# t.goto(150,20)
# t.pendown()
# t.circle(100)

# t.penup()
# t.goto(-70,20)
# t.pendown()
# t.circle(100)

# turtle.done()

# class myclass:
#     a = 10
#     b = 20

#     def myfunc(self):
#         print('Hello')

# x = myclass()

# print(x.b)

# x.myfunc()

# class student:
#     def __init__(self,name,age):
#         self.x = name
#         self.y = age
#         # print(self.x,self.y)

# Student = student('Rahim',45)

# print(Student.x)
# print(Student.y)

# class namta:
#     def __init__(self,num):
#         for i in range(1,11):
#             print(f"{num} X {i} = {num*i}")

# num2 = int(input("Enter a number : "))
# Namta = namta(num2)

# class parent:
#     a = 10
#     b = 20
#     def myfunc(self):
#         print('Hello')

# class child(parent):
#     x = 34
#     y = 4554
#     def myfunc2(self):
#         print('World')

# Parent = parent()
# Child = child()
# Child.myfunc()

# class Dog:
#     def speak(self):
#         return "Woof"
# class Cat:
#     def speak(self):
#         return "Meow"
# class Cow:
#     def speak(self):
#         return "Moo!"

# animal = [Dog(),Cat(),Cow(),Cat()]

# for i in animal:
#     print(i.speak())

# dog = Dog()
# cat = Cat()
# cow = Cow()

# def animal_sound(animal):
#     print(animal.speak())

# animal_sound(dog)
# animal_sound(cat)
# animal_sound(cow)
# animal_sound(cat)

# class Student:
#     def __init__(self,name):
#         self.x = name
#         print(f"{self.x} has been created")

#     def __del__(self):
#         print(f"{self.x} has been destroyed")

# student = Student('Rahim')

class Logger:
    def __init__(self,filename):
        self.file = open(filename,'w')
        self.file.write("This is our Test case.")
        print("Write started")
    
    def log(self,massege):
        self.file.write(massege + '\n')
    
    def __del__(self):
        self.file.write("End" + '\n')
        self.file.close()
        print('File has been closed')
    
loger = Logger("alu.txt")
loger.log('This is the massege.')
del loger 
