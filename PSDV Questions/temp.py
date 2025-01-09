import numpy as np
import time

# # Define a list and a NumPy array
# n = 1_000_000
# py_list = list(range(n))
# np_array = np.arange(n)

# # Iterating over a Python list
# start = time.time()
# for x in py_list:
#     x * 2
# end = time.time()
# print(f"Python list iteration: {end - start:.5f} seconds")

# # Iterating over a NumPy array
# start = time.time()
# for x in np_array:
#     x * 2
# end = time.time()
# print(f"NumPy array iteration: {end - start:.5f} seconds")

# start = time.time()
# arr = np.arange(1_000_000)
# result = arr * 11  # Vectorized operation
# end = time.time()
# print(f"NumPy array iteration: {end - start:.5f} seconds")

# rows = 1000
# cols = 1000
# start = time.time()
# x = [[i + j for j in range(cols)] for i in range(rows)]
# end = time.time()
# print(f"NumPy array iteration: {end - start:.5f} seconds")


# start = time.time()
# y = np.fromfunction(lambda i, j: i + j, (rows, cols), dtype=int)
# end = time.time()
# print(f"NumPy array iteration: {end - start:.5f} seconds")

# start = time.time()
# i, j = np.meshgrid(np.arange(rows), np.arange(cols), indexing='ij')
# z = i + j
# end = time.time()
# print(f"NumPy array iteration: {end - start:.5f} seconds")

