#!/home/salzatec1/miniconda3/bin/python
import numpy as np

def lagrange(X, Y):
    n = X.size
    L = np.zeros((n, n)) # (shape)

    for i in range(n):
        aux0 = np.setdiff1d(X, X[i])
        aux = [1, -aux0[0]]
        for j in range(1, n-1):
            aux = np.convolve(aux, [1, -aux0[j]])
        L[i,:] = aux / np.polyval(aux, X[i])

    coef = Y.dot(L)
    print("Lagrange interpolating polynomials:\n", L)
    print("Coef:\n", coef)
    return L, coef

def main():
    np.set_printoptions(suppress=True)
    #X = np.array([1, 2, 3, 4, 5])
    #
    #Y = np.array([1, 2, 3, 4, 5])
    X = np.array([-1, 0, 3, 4])
    
    Y = np.array([15.5, 3, 8, 1])
    L, coef = lagrange(X, Y)


if __name__=="__main__":
    main()
