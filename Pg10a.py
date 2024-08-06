#Name, index, key, zero 

try:
    print(hello)
except NameError as NE:
    print("NameError", NE)

try: 
    my_list = [1,3,4]
    print(my_list[5])
except IndexError as IE:
    print("IndexError: ", IE)

try: 
    my_dict = {'a': 1}
    print(my_dict['b'])
except KeyError as KE:
    print("KeyError: ", KE)

try:
    res = 5/0
    print(res)
except ZeroDivisionError as ZDE:
    print("ZeroDivisionError: ", ZDE)
    
