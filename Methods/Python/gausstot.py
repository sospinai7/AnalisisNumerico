#!/home/salzatec1/miniconda3/bin/python

import numpy as np
from sustreg import sustreg

def gausstot(A, b):
    det = np.linalg.det(A)
    if det == 0:
        print("Error: Determinant of A is zero")
        return

    M = np.column_stack((A, b))
    n = A.shape[0]
    M = M.astype('float')
    stack = []
    etapa = 0
    # Todas las columnas de A - 1
    for i in range(0, n - 1):
        print("Phase", etapa)
        print(M)
        print()
        etapa += 1
        submatrix = abs(M[i:,i:n])
        #print(submatrix)
        a = np.amax(submatrix)
        row, col = np.where(submatrix == a)
        row = row[0]
        col = col[0]
        #print("Row:",row,"Col:",col)
        # Cambio de fila
        if row+i != i:
            M[[row+i, i],i:] = M[[i, row+i],i:]
            print("Row change")
            print(M)
            print()
        # Cambio de columna
        if col+i != i:
            M[:,[i, col+i]] = M[:,[col+i, i]]
            stack = np.append(stack, [i, col+i])  # Agregar cambio de columna al stack
            print("Column change")
            print(M)
            print()

        # Por cada columna iterar por cada fila debajo de la diagonal
        for j in range(i+1, n):
            if M[j][i] != 0:
                # Operacion de subfila
                M[j][i:n+1] = M[j][i:] - (M[j][i]/M[i][i])*M[i][i:]

    print("Phase", etapa)
    print(M, '\n')
    stack = np.array(stack, dtype=int).reshape(-1,2)
    # Sustitucion regresiva
    x = sustreg(M)
    print("After applying back substitution\n")
    print("X before changing columns:")
    print(x)
    x = cambioCols(x, stack)
    print("X after changing columns:")
    print(x)
    return x

def cambioCols(x, stack):
    for i in range(stack.shape[0]-1,-1,-1):
        cambio = stack[i]
        aux = x[cambio[0]]
        x[cambio[0]] = x[cambio[1]]
        x[cambio[1]] = aux
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
    A = np.array(([0, 0, 1],
                [4, 2, 1],
                [0.81, 0.9, 1]))
    b = np.array([0.5, 1, 0])
    gausstot(A, b)


if __name__ == '__main__':
    main()
