print("Press:\n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\nOther: Exit")

while True:
    choice = int(input())
    a = int(input("Enter 1st operand: "))
    b = int(input("Enter 2nd operand: "))
    
    if choice == 1:
        print("Result: ", a+b)
    elif choice == 2:
        print("Result: ", a-b)
    elif choice == 3:
        print("Result: ", a*b)
    elif choice == 4:
        print("Result: ", (a/b if b!=0 else "Division by zero!"))
    else:
        break

    
        

