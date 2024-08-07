import random
import re

a = [
    str(random.randint(0,10000)) for _ in range(20)
]
res = []

for num in a:
    if re.match(r"^\d{2}$", num) or re.match(r"^\d{4}$", num):
        if int(num) % 2 != 0:
            res.append(num)
        
print(res)

