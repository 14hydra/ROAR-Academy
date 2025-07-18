import numpy as np

arr1 = np.array([[6, -9, 1], [4, 24, 8]])

print(arr1 * 2)

print(np.eye(2) @ arr1)

arr2 = np.array([[4, 3], [3, 2]])

arr3 = np.array([[-2, 3], [3, -4]])
print(arr2 @ arr3)