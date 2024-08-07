file_name = "samplefile.txt"

with open(file_name, "w") as file:
    for _ in range(3):
        line = input()
        file.write(line + '\n')

with open(file_name, 'r') as file:
    words = file.read().split()
    words.sort(key=lambda x: len(x))
    print('Longest: ' + words[-1])
    print(words[0])
