import numpy as np

m, n = map(int, input('Enter row and col: ').split())

arr = np.zeros((m,n), dtype=int)
for i in range(m):
    for j in range(n):
        num = int(input('num: '))
        arr[i][j] = num 

print(arr)

#to check dimension
print(arr.ndim)

#to access 
print(arr[0][0])
print(arr[0, 0])

#slicing 2d
#eg to reverse 
print(arr[::-1, ::-1])

#reshaping eg) 2 * 1 * 2 
threed = [
    [
        [1,2]
    ], 
    [
        [3,4]
    ]
]
threed = np.array(threed)
print(threed.shape)

#reshaping 
print(threed.reshape(2,2))

#flattening
print(threed.reshape(-1))

#principal diagonal
print(arr.diagonal())
print(np.diag(arr))

#sorting 2d array 
#numpy.sort(arra) will not modify the original but array.sort() will

print(np.sort(arr)) # sorts each row, default axis = 1 i.e row
print(np.sort(arr, axis=0)) # sorts each col

print(np.sort(arr, axis=None)) #sorts the entire 2d array but flattens
print(np.sort(arr, axis=None).reshape(arr.shape)) #sorts the entire 2d array retaining its original shape
print(np.sort(arr, axis=None)[::-1].reshape(arr.shape)) # descending



