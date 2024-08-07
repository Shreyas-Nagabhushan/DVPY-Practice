items = [] 
n = 3 
for _ in range(n):
    items.append(input())
tup = tuple(items)

print(tup)
#adding an item to tuple
items = list(tup)
items.append(input("NEw item: "))
tup = tuple(items)
print(tup)
print()

print(len(tup))
print("hello" in tup)
print(tup[2])