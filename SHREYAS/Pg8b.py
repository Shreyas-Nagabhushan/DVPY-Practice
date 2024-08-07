file_name = "samplefile.txt"

with open(file_name, "w") as file:
    for _ in range(3):
        line = input()
        file.write(line + '\n')

with open(file_name, 'r') as file:
    content = file.read()
    upper = lower = digits = 0
    for ch in content:
        if ch.isupper():
            upper += 1 
        if ch.islower():
            lower += 1 
        if ch.isdigit():
            digits += 1 
print(upper)
print(lower)
print(digits)