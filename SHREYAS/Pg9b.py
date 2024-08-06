#handling multiple exceptions using try except else finally 

n = int(input('Enter the denominator'))
name = True 

try:
    res = 10/n
    if name: 
        print(bs)
except ZeroDivisionError as ZE:
    print(ZE)
except NameError as NE:
    print(NE)
else:
    print("You are intelligent")
finally:
    print("I am done with this B.S")

print("WTF am i doing here")