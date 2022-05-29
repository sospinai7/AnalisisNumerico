#!/home/salzatec1/miniconda3/bin/python

import numpy as np
from sustreg import sustreg
from sustprog import sustprog

def lusimpl(A, b):
    det = np.linalg.det(A)
    if det == 0:
        print("Error: Determinant of A is zero")
        return

    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros((n, n))
    M = A
    M = M.astype('float')
    stack = []
    etapa = 0
    print("Phase", etapa)
    print("M:\n", M)
    print()
    etapa += 1
    # Todas las columnas de A - 1
    for i in range(0, n - 1):
        # Por cada columna iterar por cada fila debajo de la diagonal
        for j in range(i+1, n):
            if M[j][i] != 0:
                # Operacion de subfila
                if M[i][i] == 0:
                    print("Error: Division by zero")
                    return
                L[j][i] = M[j][i]/M[i][i]
                M[j][i:n+1] = M[j][i:] - (M[j][i]/M[i][i])*M[i][i:]

        U[i, i:n] = M[i, i:n]
        U[i+1, i+1:n] = M[i+1, i+1:n]
        print("Phase", etapa)
        print("M:\n", M)
        print("L:\n", L)
        print("U:\n", U)
        print()
        etapa += 1

    U[n-1][n-1] = M[n-1][n-1]
    stack = np.array(stack, dtype=int).reshape(-1,2)
    # Sustitucion regresiva
    print("After applying forward and backward substitution\n")
    z = sustprog(np.column_stack((L, b)))
    x = sustreg(np.column_stack((U, z)))
    print("X:\n", x)
    return x

def main():
    #size = 4
    #A = np.random.rand(size, size)
    #b = np.random.rand(size)
    #A = np.array(([2, -1, 0, 3], 
    #             [1, 0.5, 3, 8], 
    #             [0, 13, -2, 11], 
    #             [14, 5, -2, 3]))
    #b = np.array([1, 1, 1, 1])
    #A = np.array(([0, 0, 1],
    #            [4, 2, 1],
    #            [0.81, 0.9, 1]))
    #b = np.array([0.5, 1, 0])
    #A = np.array(([3, 1, 1],
    #            [2, 3, 1],
    #            [4, 8, 1]))
    #b = np.array([0.5, 1, 0])
    A = np.array(([4, -1, 0, 3],
                  [1, 15.5, 3, 8],
                  [0, -1.3, -4, 1.1],
                  [14, 5, -2, 30]))
    b = np.array([1, 1, 1, 1])
    x = lusimpl(A, b)
    print("X:\n", x)


if __name__ == '__main__':
    main()
