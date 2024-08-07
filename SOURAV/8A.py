import random
import re
import numpy as np

a = [
    str(random.randrange(0,9999)) for _ in range(20)
]

twos = []
fours = []

for num in a:

    if re.match(r"^[0-9]{2}$", num) and int(num)%2!=0:
        twos.append(num)
    
    if re.match(r"^[0-9]{4}$", num) and int(num)%2!=0:
        fours.append(num)
        
print(twos)
print(fours)

