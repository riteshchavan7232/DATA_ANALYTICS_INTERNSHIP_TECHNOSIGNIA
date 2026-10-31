
# NUMPY

#1 Import NumPy
import numpy as np

print("NumPy imported successfully")


# NUMPY ARRAYS

#1 One dimensional array
arr = np.array([10, 20, 30, 40, 50])

print(arr)


#2 Two dimensional array
arr = np.array([[10, 20, 30], [40, 50, 60]])

print(arr)


#3 Multidimensional array
arr = np.array([[[10, 20], [30, 40]], [[50, 60], [70, 80]]])

print(arr)


#4 Array dimensions
arr = np.array([[10, 20, 30], [40, 50, 60]])

print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)


# INDEXING AND SLICING

#1 Indexing
numbers = np.array([10, 20, 30, 40, 50])

print(numbers[0])
print(numbers[2])
print(numbers[-1])


#2 Slicing
numbers = np.array([10, 20, 30, 40, 50])

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])


#3 Two dimensional array indexing
numbers = np.array([[10, 20, 30], [40, 50, 60]])

print(numbers[0, 0])
print(numbers[1, 2])


# FILTERING

#1 Filter values greater than 20
numbers = np.array([10, 20, 30, 40, 50])

result = numbers[numbers > 20]

print("Filtered values:", result)


#2 Filter values less than 30
numbers = np.array([10, 20, 30, 40, 50])

result = numbers[numbers < 30]

print("Filtered values:", result)


# RESHAPING ARRAYS

#1 Reshape one dimensional array
numbers = np.array([10, 20, 30, 40, 50, 60])

result = numbers.reshape(2, 3)

print(result)


#2 Reshape into three rows
numbers = np.array([10, 20, 30, 40, 50, 60])

result = numbers.reshape(3, 2)

print(result)


# NUMERICAL CALCULATIONS

#1 Calculate sum
numbers = np.array([10, 20, 30, 40, 50])

total = np.sum(numbers)

print("Total:", total)


#2 Calculate mean
numbers = np.array([10, 20, 30, 40, 50])

average = np.mean(numbers)

print("Average:", average)


#3 Find minimum value
numbers = np.array([10, 20, 30, 40, 50])

minimum = np.min(numbers)

print("Minimum value:", minimum)


#4 Find maximum value
numbers = np.array([10, 20, 30, 40, 50])

maximum = np.max(numbers)

print("Maximum value:", maximum)


#5 Calculate standard deviation
numbers = np.array([10, 20, 30, 40, 50])

result = np.std(numbers)

print("Standard deviation:", result)


# PYTHON LIST VS NUMPY ARRAY

#1 Python list calculation
numbers = [10, 20, 30, 40, 50]

result = []

for number in numbers:
    result.append(number * 2)
print("Python list:", result)


#2 NumPy array calculation
numbers = np.array([10, 20, 30, 40, 50])
result = numbers * 2
print("NumPy array:", result)


#3 Addition using NumPy
a = np.array([10, 20, 30])
b = np.array([5, 10, 15])
result = a + b
print("Addition:", result)


#4 Multiplication using NumPy
a = np.array([10, 20, 30])
b = np.array([2, 3, 4])

result = a * b
print("Multiplication:", result)
