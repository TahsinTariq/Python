import timeit

print(timeit.timeit('''print("stuff")
''', number=10000))

# import numpy as np
#
# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
#
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)
#
# arr = np.array([[[1, 2, 3], [4, 5, 6]],[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]], ndmin=5)
#
# print(arr)
# print('shape of array :', arr.shape)

# d = [[1, 2], [1, 3], [1, 1], [2, 4], [2, 1]]
# print(sorted(d, key= lambda x: ()))
# print(input("write something"))
