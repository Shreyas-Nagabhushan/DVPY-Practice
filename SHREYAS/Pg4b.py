import re

text = "hello i am shawn mur!phy. i am 19 years old"

vowels = re.findall(r"[aeiouAEIOU]", text)
consonants = re.findall(r"[^aeiouAEIOU0-9\s\.\!\,\?]", text)
digits = re.findall(r"\d", text)

print(vowels)
print(consonants)
print(digits)