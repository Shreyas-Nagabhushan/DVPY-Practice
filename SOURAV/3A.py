n = int(input("Enter the number of words: "))
d = {}
for i in range(n):
    d.update({
        input("Enter word: "): input("Enter meaning: ")
    })

print("1) Add new word\n2) Search and get meaning\n3) Find words with same meaning\n4) Remove a word\n5) Display sorted\nOther: Exit")

while True:
    choice = int(input("Enter choice: "))

    if choice == 1:
        w = input("Enter the new word: ")
        m = input("Enter meaning: ")
        d[w] = m
    
    elif choice == 2:
        w = input("Enter word: ")
        if w in d:
            print("Meaning: ", d[w])
        else:
            print("Word doesn't exist! ")
    
    elif choice == 3: 
        m = input("Enter meaning: ")
        for w in list(d.keys()):
            if d[w] == m:
                print(w, end=" ")
        print()
    
    elif choice == 4:
        w = input("Enter word: ")
        if w in d:
            del d[w]
    
    elif choice == 5:
        w = list(d.keys())
        w.sort()
        for word in w:
            print(word, " : ", d[word])
    else:
        break
    