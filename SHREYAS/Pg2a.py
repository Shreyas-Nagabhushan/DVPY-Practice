import math
def get_sieve(upper_limit):
    sieve = [True for _ in range(upper_limit)]
    for i in range(2, int(math.sqrt(upper_limit)) + 1):
        for j in range(i*i, upper_limit, i):
            sieve[j] = False 
    return sieve
print(get_sieve(100000)[29])
    