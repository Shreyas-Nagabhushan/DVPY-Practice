# def binary_search(arr, left, right, target):
#     if left > right:
#         return -1
#     mid = (left + right)//2
#     if arr[mid] == target:
#         return mid 
#     elif arr[mid] > target:
#         return binary_search(arr, left, mid-1, target)
#     else:
#         return binary_search(arr, mid+1, right, target) 
    
f = (lambda arr, left, right, target: print(-1) if left > right else print((left+right)//2) if arr[(left+right)//2] == target else f(arr, (left+right)//2+1, right, target) if target > arr[(left+right)//2] else f(arr, left, (left+right)//2-1, target))([1,2,3], 0, 2, 2)

# if __name__ == "__main__":
#     array = [] 
#     n = int(input())
#     for _ in range(n):
#         array.append(int(input()))
#     target = int(input('target: '))
#     print(binary_search(array, 0, n-1, target))
