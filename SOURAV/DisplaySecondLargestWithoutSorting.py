# (lambda arr: print([max(arr), max([i for i in arr if i!=max(arr)])]))(list(map(int, input('Enter elements: ').split()))) 

def find_largest(arr):
    print('Largest: ', max(arr))
    cpy = [num for num in arr if num != max(arr)]
    print('Second Largest: ', max(cpy))

n = int(input('Enter number of elements: '))
arr = [int(input('Enter number: ')) for _ in range(n)]
find_largest(arr)