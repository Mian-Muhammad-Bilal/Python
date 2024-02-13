import numpy as np
# Question1
# Create a 1D NumPy array
# arr1 = np.array([1, 2, 3, 4, 5])

# Create a 2D NumPy array
# arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(f"First element of arr1: '{arr1[0]}' Last element of arr1: '{arr1[-1]}'")
# print("Element in the second row and third column of arr2:", arr2[1], arr2[2])

# # Calculate the determinant and inverse of arr1

# # Reshape arr1 to be a 2D array for determinant calculation
# n_arr1 = arr1.reshape(1, -1)
# print(n_arr1.ndim)
# det_arr1 = np.linalg.det(n_arr1)
# Create a diagonal matrix from arr1 for inverse calculation
# inv_arr1 = np.linalg.inv(np.diag(arr1))

# # Calculate the determinant and inverse of arr2
# det_arr2 = np.linalg.det(arr2)
# inv_arr2 = np.linalg.inv(arr2)

# # Print results
# print("\nDeterminant of arr1:", det_arr1)
# print("\nInverse of arr1:\n", inv_arr1)
# print("\nDeterminant of arr2:", det_arr2)
# print("\nInverse of arr2:\n", inv_arr2)

# Question2


# Create a 1D NumPy array named arr1 with elements [1, 2, 3, 4, 5].
arr1 = np.array([1, 2, 3, 4, 5])

# # Create a 2D NumPy array named arr2 with elements [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# # Add 10 to each element of arr1.
# arr1_added_10 = arr1 + 10
# print("arr1 after adding 10 to each element:")
# print(arr1_added_10)

# # Multiply each element of arr2 by 2.
# m_arr2 = arr2 * 2
# print("\narr2 after multiplying each element by 2:")
# print(m_arr2)

# # Calculate the square root of each element in arr1.
# sqrt_arr1 = np.sqrt(arr1)
# print("\nSquare root of each element in arr1:")
# print(sqrt_arr1)

# Create a 2D array named matrix with elements [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

matrix = matrix + np.array([10, 20, 30])
print("Matrix after adding [10, 20, 30] to each row using broadcasting:")
print(matrix)

arr2_transpose = np.dot(arr2, arr2.T)
print("\nResult of multiplying arr2 by its transpose:")
print(arr2_transpose)

arr2_det = np.linalg.det(arr2)
print("\nDeterminant of arr2:")
print(arr2_det)

# arr2_in = np.linalg.inv(arr2)
# print("\nInverse of arr2:")
# print(arr2_in)
