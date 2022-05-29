#!/home/salzatec1/miniconda3/bin/python

import numpy as np
from sustreg import sustreg

def gseidel(A, b, x0, tol, Nmax):
    if Nmax < 0:
        print("Error: Number of iterations can not be less than 0")
        return
    
    if tol < 0:
        print("Error: Tolerance can not be less than 0")
        return
    det = np.linalg.det(A) # Determinant of matrix
    if det == 0:
        print("Error: Determinant of matrix is 0")
        return

    diagonal = np.diagonal(A)
    nozeros = np.count_nonzero(diagonal)

    if nozeros != A.shape[0]:
        print("Error: There are zeros in the diagonal of the matrix 'A'")
        return

    D = np.diag(np.diag(A))
    L = -np.tril(A)+D
    U = -np.triu(A)+D
    
    T = np.linalg.inv(D-L).dot(U)
    C = np.linalg.inv(D-L).dot(b)
    print("T:\n", T)
    print("C:\n",C)
    eig = np.max(np.abs(np.linalg.eig(T)[0]))
    print("Espectral radius:\n", eig)
    print()
    if eig > 1:
        print("Since the espectral radius is greather than 1 this method will not encounter a solution for this matrix")
        return
    xant = x0
    E = 1000
    cont = 0

    while E>tol and cont<Nmax:
        np.set_printoptions(precision=8, suppress=True)
        print("{i:2d} | X{i} = {xant} | E = {Err:.1E}".format(i=cont, xant=xant, Err=E))
        xact = T.dot(xant) + C
        E = np.linalg.norm(xant-xact)
        xant = xact
        cont += 1

    if E>tol or cont == Nmax:
        print("{i} | X{i} = {xant} | E = {Err:.1E}".format(i=cont, xant=xant, Err=E))
        print("This method can not get solution to the matrix")
    else:
        print("{i} | X{i} = {xant} | E = {Err:.1E}".format(i=cont, xant=xant, Err=E))

def main():
    #size = 4
    #A = np.random.rand(size, size)
    #b = np.random.rand(size)
    #A = np.array(([2, -1, 0, 3], 
    #             [1, 0.5, 3, 8], 
    #             [0, 13, -2, 11], 
    #             [14, 5, -2, 3]))
    #b = np.array([1, 1, 1, 1])
    #A = np.random.rand(3,3)
    #A = np.array(([9, 1, 2],
    #            [1, 6, 5],
    #            [2, 5, 6]))
    #b = np.array([1,1,1])
    #A = np.array(([4, -1, 0, 3],
    #              [1, 15.5, 3, 8],
    #              [0, -1.3, -4, 1.1],
    #              [14, 5, -2, 30]))
    A = np.array(([300, 6, 100, 400],
                  [6, -100, 300, -35],
                  [100, 300, 200, 14],
                  [400, -35, 14, 300]))
    b = np.array([1, 1, 1, 1])
    x0 = np.array([0, 0, 0, 0])
    gseidel(A, b, x0, 1e-7, 100)


if __name__ == '__main__':
    main()
