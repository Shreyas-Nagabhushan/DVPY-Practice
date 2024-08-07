#name error
#index error
#zero division error
#key error

print("1) NameError\n2) IndexError\n3) ZeroDivisionError\n4) KeyError\nOther: Exit")

while True:
    choice = int(input("Enter the type of exception to generate: "))
    
    try:
        if choice == 1:
            func()
        if choice == 2:
            a = [1,2,3]
            print(a[3])
        if choice == 3:
            x = 2/0
        if choice == 4:
            d = {}
            print(d["somekey"])
        else:
            break

    except NameError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except IndexError as e:
        print(e)
    except KeyError as e:
        print(e)