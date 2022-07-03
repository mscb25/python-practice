import numpy as np

#array = collection of python nums
# vector = 1d python array

#to create array:

x = np.array([2, 4, 6, 8, 10])

print(x)


#arrange() can also be used to initialize arrays

print(np.arange(1, 7)) #array from 1 up to (but not including) 7

print(np.arange(6)) #array from 0 up to (but not including) 6

print(np.arange(1, 10, 3)) #array from 1 up to (but not including) 10 counting by 3

# multi-dimensional arrays are matricies

y = np.array([[2, 4, 6, 8, 10],[2, 4, 6, 8, 10]])
print(y)

print(y.shape)
print(y.size)

print("bytes per elm: ", y.itemsize)
print("total bytes: ", y.nbytes)
print("dimensions: ", y.ndim)
print("data type: ", y.dtype)


# can perform operations on elements in an array

# scalar addition
print(x +7)

# mean and standard dev

print("mean = ", np.mean(x))
print("standard dev = ", np.std(x))

# to find the greatest and smallest numbers in array

print("min = ", np.min(x))
print("max = ", np.max(x))

# sum and product

print("sum = ", np.sum(x))
print("product = ", np.prod(x))

# return array of cumulative sum and product

print("cumulative sum array = ", np.cumsum(x))
print("cumulative product array = ", np.cumprod(x))

z = np.arange(20)
print(z)



print("values less than 8: ", z[z < 8])

#replacing all vals less than 8 with 0
z[z < 8] = 0
print(z)

#for multiple conditions, and = &, or = |

# to determine if any element is positive

if (z > 0).any():
    print("there is a positive num in this array")
else:
    print("no element is positive")


# to determine if all the elements are odd

if (z % 2 == 1).all():
    print("all the elements in this array are odd")
else:
    print("not every element is odd")

#to create a copy of an array

a = np.copy(z)
print(a)

                        
