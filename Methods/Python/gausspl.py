#!/home/salzatec1/miniconda3/bin/python

import numpy as np
from sustreg import sustreg

def gausspl(A, b):
    np.set_printoptions(precision=3)
    det = np.linalg.det(A)

    if det == 0:
        print("Error: Determinant of A is zero")
        return

    M = np.column_stack((A, b))
    n = A.shape[0]
    #print("Rows: ", M.shape[0], ",", "Columns:", M.shape[1])
    M = M.astype('float')
    #print(M.dtype)

    etapa = 0
    # Todas las columnas de A - 1
    for i in range(0, n - 1):
        print("Phase", etapa)
        print(M)
        etapa += 1
        if M[i][i] == 0:
            change = False
            for c in range(i+1, n):
                if M[c][i] != 0:
                    M[[c, i],:] = M[[i,c],:]
                    change = True
                    break
            if change:
                print("Phase", etapa)
                print(M)
                etapa += 1
            else:
                print('This equation system can not be resolved by this method')
                return


        # Por cada columna iterar por cada fila debajo de la diagonal
        for j in range(i+1, n):
            if M[j][i] != 0:
                # Operacion de subfila
                M[j][i:n+1] = M[j][i:] - (M[j][i]/M[i][i])*M[i][i:]

    print("Phase", etapa)
    print(M, '\n')
    # Sustitucion regresiva
    x = sustreg(M)
    print("After applying backward substitution\n")
    print("X:")
    print(x)
    return x

def main():
    #A = np.array(([1,2,3], [4,4,6], [7,8,9]), dtype=float)
    #b = np.array([4, 9,9])
    #size = 4
    #A = np.random.rand(size, size)
    #b = np.random.rand(size)
    A = np.array(([2, -1, 0, 3], 
                 [1, 0.5, 3, 8], 
                 [0, 13, -2, 11], 
                 [14, 5, -2, 3]))
    b = np.array([1, 1, 1, 1])
    gausspl(A, b)


if __name__ == '__main__':
    main()
