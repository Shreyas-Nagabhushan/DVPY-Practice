passwd = {
    'Rahul': 'genius',
    'Kumar': 'smart',
    'Ankita': 'intelligent'
}
print("Items: ")
print(passwd.items())
print()
print("Keys: ")
print(passwd.keys())
print()
print("Values: ")
print(passwd.values())

u = input("Enter the user whose password you want to retrive: ")

if u in passwd:
    print(passwd[u])
else:
    print("User doesn't exist.")

u = input("Enter the user whose password is to be changed: ")

if u in passwd:
    p = input("Enter new password: ")
    passwd[u] = p
else:
    print("User doesn't exist.")

print("Resultant dictionary: ")
print(passwd)