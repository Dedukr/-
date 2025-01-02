import numpy as np
import math
# Generate the matrix
n = 7  # Size of the grid
matrix = np.zeros((n, n), dtype=int)

# Fill in the values
for i in range(n):
    for j in range(n -i -1,n):
            matrix[i][j] = j - (n-i-1)+1

print(matrix)