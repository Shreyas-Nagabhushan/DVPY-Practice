try:
    a = int(input("Enter operand 1: "))
    b = int(input("Enter operand 2: "))
    x = a/b
    print(x)
    arr = [int(input()) for _ in range(int(input("Enter the number of elements in your list: ")))]
    i = int(input("Enter an index to access: "))
    print(arr[i])

except ZeroDivisionError:
    print("Zero division error")

except IndexError:
    print("Index is invalid")

else:
    print("No exceptions")

finally:
    print("In finally block")