l = []
n = int(input("Enter the number of strings: "))
for i in range(n):
    s = input(f"Enter string {i+1}: ")
    l.append((s,len(s)))
l.sort(key= lambda x:x[1])
print(l)