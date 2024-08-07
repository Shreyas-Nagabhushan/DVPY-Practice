import math
def is_prime(n):
    if n <=1:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, round(math.sqrt(n)) + 1, 2):
        if n%i == 0:
            return False
    return True

low = int(input("Enter range start: "))
high = int(input("Enter range end: "))

for i in range(low, high+1):
    if(is_prime(i)):
        print(i)
        