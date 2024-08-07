import re

text = ""

print("Enter some text: ")

while True:
    line = input()
    if line!= "":
        text += (line + "\n")
    else:
        break

print("Number of vowels: ", len(re.findall(r"[AEIOUaeiou]", text)))
print("Number of consonants: ", len(re.findall(r"[B-DF-HJ-NP-TV-Zb-df-hj-np-tv-z]", text)))
print("Number of digits: ", len(re.findall(r"[0-9]", text)))