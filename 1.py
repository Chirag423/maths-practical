import numpy as np
vector = np.array([10,11,12])
print("original vector", vector)

matrix = np.array([[10,11,12],[11,14,15],[16,17,18]])
print("original matrix", matrix)

tvector = vector.T
print("transpose of vector",tvector)

tmatrix = matrix.T
print("transpose of matrix",tmatrix)
