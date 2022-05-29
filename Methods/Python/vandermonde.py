#!/home/salzatec1/miniconda3/bin/python
import numpy as np
from gausstot import gausstot

def vandermonde(X, Y):
    n = X.size
    A = np.zeros((n, n)) # (shape)
    X = np.matrix.transpose(X)

    for i in range(n):
        A[:,i] = np.matrix.transpose(np.power(X, (n-i-1)))

    coef = gausstot(A, np.matrix.transpose(Y))

    print("A:\n", A)
    print("Coef:\n", coef)
    return coef

def main():
    #X = np.array([0, 2, 3, 4, 5, 6, 7])
    #
    #Y = np.array([1.1247, -0.8540, 0.5864, 1, -0.9062, 0.9081, -0.2700])
    #X = np.array([-1, 0, 3, 4])
    #
    #Y = np.array([15.5, 3, 8, 1])
    X = np.array([0.5, 1, 3, 5])
    
    Y = np.array([-2.835, -0.48, -2.56, 12.96])
    coef = vandermonde(X, Y)

if __name__=="__main__":
    main()
