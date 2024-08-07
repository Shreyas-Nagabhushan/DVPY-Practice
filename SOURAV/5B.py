text = ""

print("Enter some text: ")

while True:
    line = input()
    if line!= "":
        text += (line + "\n")
    else:
        break

with open("file.txt", 'w') as file:
    file.write(text)

with open("file.txt", "r") as file:
    text = file.read()


text = text.replace("\n", " ")
text = text.strip()
text = text.split(" ")

longest = max(text, key= lambda x: len(x))
print("Longest word: ", longest, ": ", len(longest), " characters.")

shortest = min(text, key= lambda x: len(x))
print("Shortest word: ", shortest, ": ", len(shortest), " characters.")

