#!/home/salzatec1/miniconda3/bin/python
import numpy as np
from gausstot import gausstot

def trazlin(X, Y):
    n = X.size
    m = 2*(n-1)
    A = np.zeros((m, m)) # (shape)
    b = np.zeros(m)
    coef = np.zeros((n-1, 2))
    etapa = 0
    print("Phase:", etapa)
    print("A:\n", A)
    print("b:\n", b)
    print()
    etapa +=1

    for i in range(n - 1):
        A[i+1, [2*i, 2*i+1]] = np.array([X[i+1], 1])
        b[i+1] = Y[i+1]

    A[0, [0, 1]] = np.array([X[0], 1])
    b[0] = Y[0]

    print("Phase:", etapa)
    print("A:\n", A)
    print("b:\n", b)
    print()
    etapa +=1

    for i in range(1, n-1):
        A[n+i-1, 2*i-2:2*i+2] = np.array([X[i], 1, -X[i], -1])
        b[n+i-1] = 0

    print("Phase:", etapa)
    print("A:\n", A)
    print("b:\n", b)
    print()

    print("Start - GAUSSTOT")
    Saux = gausstot(A, b)
    print("Finish - GAUSSTOT")

    for i in range(n-1):
        coef[i,:] = Saux[[2*i, 2*i+1]]
    
    print("Coef:\n", coef)
    
    return coef

def main():
    #X = np.array([1, 2, 3, 4, 5, 6, 7])
    #Y = np.array([1.1247, -0.8540, 0.5864, 1, -0.9062, 0.9081, -0.2700])
    #X = np.array([1, 2, 3, 4, 5])
    #Y = np.array([1, 2, 3, 4, 5])
    X = np.array([-1, 0, 3, 4])
    
    Y = np.array([15.5, 3, 8, 1])
    coef = trazlin(X, Y)
    print("Coef:\n", coef)

if __name__=="__main__":
    main()
