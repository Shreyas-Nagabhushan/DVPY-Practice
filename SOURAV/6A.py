def binary_search(a, key):
    start = 0
    end = len(a)-1
    
    while start <= end:
        mid = (start + end)//2

        if a[mid] == key:
            return mid
        elif a[mid] > key:
            end = mid-1
        else:
            start = mid+1
    return -1

a = [int(input(f"Enter element {i+1}: ")) for i in range(int(input("Enter the number of elements: ")))]
a.sort()
print("Sorted array: ", a)
result = binary_search(a, int(input("Enter the search element: ")))
print(f"Found at {result}" if result != -1 else "Element not found")