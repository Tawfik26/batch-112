print("Welcome to the calculator (budget versor)")
B=input("Do you want to use the calculator?:[yes/no]\n")
button=B.lower()
while True:
    if button == "no":
        print("Thank you, goodbye.")
        break
    elif button != "yes" and button != "no":
        print("Invalid input, please try either yes or no. Thank you.")
        break
    elif button == "yes":
        answer=input("What do you want to do?[(+)/(-)/(*)/(/)]:\n")

        if answer == "+" :
            answer=input("How many numbers do you want to sum?[2/3/4]\n")
            if answer == "2":
                ak=int(input("Input your first number: "))
                dui=int(input("Input your second number: "))
                print("sum is: ", ak+dui)
                    
            elif answer == "3":
                ak1=int(input("Input your first number:"))
                dui1=int(input("Input your second number:"))
                tin1=int(input("Input your second number:"))
                print("sum is:", ak1+dui1+tin1)
                    
            elif answer == "4":
                ak2=int(input("Input your first number: "))
                dui2=int(input("Input your second number: "))
                tin2=int(input("Input your second number: "))
                char2=int(input("Input your second number: "))
                print("sum is:", ak2+dui2+tin2+char2)
                    
            else:
                print("Error (do not support)")
                        
        elif answer == "-":
            ak3=int(input("Input your first number: "))
            dui3=int(input("Input your second number: "))
            print("difference is:", ak3-dui3)
                
        elif answer == "*":
            answer=input("How many numbers do you want to multiply?[2/3/4]\n")
            if answer == "2":
                ak4=int(input("Input your first number: "))
                dui4=int(input("Input your second number: "))
                print("Result is: ", ak4*dui4)
                    
            elif answer == "3":
                ak5=int(input("Input your first number:"))
                dui5=int(input("Input your second number:"))
                tin5=int(input("Input your second number:"))
                print("Result is:", ak5*dui5*tin5)
                    
            elif answer == "4":
                ak6=int(input("Input your first number: "))
                dui6=int(input("Input your second number: "))
                tin6=int(input("Input your second number: "))
                char6=int(input("Input your second number: "))
                print("Result is:", ak6*dui6*tin6*char6)
                    
            else:
                print("Error (do not support)")
                        
        elif answer == "/":
            ak7=int(input("Input your first number: "))
            dui7=int(input("Input your second number: "))
            if dui7 == 0:
                print("Error, cannot devide by zero.")
            else:
                print("result is:", ak7/dui7)
                    
        else:
            print("Error (This calculator do not support this feature. Apologizing for the inconvenience. Thank you.)")
   
        ag=input("Do you want to use the calculator again?[yes/no]\n")
        again=ag.lower()
        if again == "no":
            print("Thank you for your time.")
            break
        elif again == "yes":
            continue
        else:
            print("Invalid input, please try either yes or no. Thank you.")
            break


                    
    
