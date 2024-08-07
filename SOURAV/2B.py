n = int(input("Enter the number of subjects: "))
subjects = []

print("Enter the subject names: ")
for i in range(n):
    subjects.append(input())

print("Displaying the list using a for loop")
for e in subjects:
    print(e, end="\t")
print()

print("2nd and 5th elements are: ")
print(subjects[1], " , ", subjects[4])

print("First four elements: ")
print(subjects[:4])

print("Last four elements: ")
print(subjects[-4:])

if "Python Programming Lab" in subjects:
    print("Yes, Python Programming Lab is available.")
else:
    print("No, Python Programming Lab is not available.")

sub = input("Enter a subject to append: ")
subjects.append(sub)

print("Subjects is now: ")
print(subjects)

sub = input("Enter a subjec to insert: ")
i = int(input("Enter the index to insert it in: "))
subjects.insert(i, sub)

print("Subjects is now: ")
print(subjects)

sub = input("Enter a subject to remove: ")
subjects.remove(sub)

print("Subjects is now: ")
print(subjects)

pop_by_index = input("Do you want to pop by index: (Press Y for yes): ")

if pop_by_index.lower() == "y":
    i = int(input("Enter the index to pop from: "))
    subjects.pop(i)
else:
    subjects.pop()

print("Subjects is now: ")
print(subjects)

