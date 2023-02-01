import numpy as np
matrix = np.array([[1,2,3],[4,6,5],[7,8,9]])
print(matrix)
rank = np.linalg.matrix_rank(matrix)
print("rank of the matrix = ",rank)
