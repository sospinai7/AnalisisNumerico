
from sustreg import sustreg
from sustprog import sustprog
import numpy as np

def crout(A, b):
    det = np.linalg.det(A)
    if det == 0:
        print("Error: Determinant of A is zero")
        return
    n = np.array(A.shape[0])
    L = np.eye(n)
    U = np.eye(n)
    etapa = 0
    print("Phase:", etapa)
    print("A:\n", A)
    print()
    etapa +=1

    for i in range(0, n-1):
        for j in range(i, n):
            L[j][i] = A[j][i] - L[j, 0:i].dot( np.matrix.transpose(U[0:i,i]))

        for j in range(i+1, n):
            U[i][j] = np.divide((A[i][j] - L[i, 0:i].dot( np.matrix.transpose(U[0:i,j]))), L[i][i])

        print("Phase:", etapa)
        print("L:\n", L)
        print("U:\n", U)
        print()
        etapa +=1

    L[n-1][n-1] = A[n-1][n-1] - L[n-1, 0:n-1].dot( np.matrix.transpose(U[0:n-1,n-1]))
    print("Phase:", etapa)
    print("L:\n", L)
    print("U:\n", U)
    z= sustprog(np.column_stack((L, b)))
    x = sustreg(np.column_stack((U, z)))
    print("After applying forward and backward substitution\n")
    print("X:\n", x)

    return x

def main():
    #A = np.array(([3, 1, 1],
    #            [2, 3, 1],
    #            [4, 8, 1]))
    #b = np.array([0.5, 1, 0])
    A = np.array(([4, -1, 0, 3],
                  [1, 15.5, 3, 8],
                  [0, -1.3, -4, 1.1],
                  [14, 5, -2, 30]))
    b = np.array([1, 1, 1, 1])

    x = crout(A, b)
    print("X:\n", x)

if __name__=="__main__":
    main()
