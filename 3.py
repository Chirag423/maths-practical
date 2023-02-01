import numpy as np

def cofactor(A):
    if A.shape[0] != A.shape[1]:
        raise ValueError("The matrix must be square.")
    n = A.shape[0]
    C = np.zeros_like(A)

    for i in range(n):
        for j in range(n):
            submatrix = np.delete(np.delete(A, i, axis=0), j, axis=1)

            # Find the cofactor
            C[i][j] = (-1) ** (i + j) * np.linalg.det(submatrix)

    return C

def determinant(A):

    if A.shape[0] != A.shape[1]:
        raise ValueError("The matrix must be square.")
    n = A.shape[0]

    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    det = 0

    for i in range(n):
        cof = cofactor(A)[0][i]
        det += (-1) ** i * A[0][i] * cof

    return det

def adjoint(A):
    C = cofactor(A)
    return C.T

def inverse(A):
    det = determinant(A)

    if det == 0:
        raise ValueError("The matrix is singular and has no inverse.")

    adj = adjoint(A)

    return adj / det
  
A = np.array([[1, 2, -4], [4, 5, -3], [6, -8, 5]])

C = cofactor(A)
print("the cofactor of the matrix is ",C)

det = determinant(A)
print("determinant of the matrix is", det)

adj = adjoint(A)
print(adj)

inv = inverse(A)
print("inverse of the matrix is" ,inv)
