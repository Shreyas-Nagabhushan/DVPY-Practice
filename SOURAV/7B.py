import numpy as np

r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))

arr = np.array([[input() for _ in range(c)] for _ in range(r)])
print(arr)
print(arr[::-1])
print(arr.diagonal())

print(np.sort(arr))
print(np.sort(arr)[::-1, ::-1])