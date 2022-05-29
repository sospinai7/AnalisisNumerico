#!/home/salzatec1/miniconda3/bin/python
import numpy as np
from gausstot import gausstot
from gausspl import gausspl

def trazcuad(X, Y):
    n = X.size
    m = 3*(n-1)
    A = np.zeros((m, m)) # (shape)
    b = np.zeros(m)
    coef = np.zeros((n-1, 3))
    etapa = 0
    print("Phase:", etapa)
    print("A:\n", A)
    print("b:\n", b)
    print()
    etapa += 1

    # Condiciones de interpolacion
    for i in range(n - 1):
        A[i+1, 3*i:3*i+3] = np.array([X[i+1]**2, X[i+1], 1])
        b[i+1] = Y[i+1]

    A[0, 0:3] = np.array([X[0]**2, X[0], 1])
    b[0] = Y[0]
    print("Phase:", etapa)
    print("A:\n", A)
    print("b:\n", b)
    print()
    etapa += 1

    # Condiciones de continuidad
    for i in range(1, n-1):
        A[n+i-1, 3*i-3:3*i+3] = np.array([X[i]**2, X[i], 1, -X[i]**2, -X[i], -1])
        b[n+i-1] = 0
    print("Phase:", etapa)
    print("A:\n", A)
    print("b:\n", b)
    print()
    etapa += 1

    # Condiciones de suavidad
    for i in range(1, n-1):
        A[2*n+i-3, 3*i-3:3*i+3] = np.array([2*X[i], 1, 0, -2*X[i], -1, 0])
        b[2*n+i-3] = 0

    A[m-1, 0] = 2
    b[m-1] = 0
    print("Phase:", etapa)
    print("A:\n", A)
    print("b:\n", b)
    print()
    etapa += 1

    print("Start - GAUSSTOT")
    Saux = gausstot(A, b)
    print("End - GAUSSTOT")

    for i in range(n-1):
        coef[i,:] = Saux[3*i:3*i+3]

    print("Phase:", etapa)
    print("A:\n", A)
    print("b:\n", b)
    print()
    print("Coef:\n", coef)
    return coef

def main():
    #np.set_printoptions(suppress=True)
    #X = np.array([1, 2, 3, 4, 5, 6, 7])
    #Y = np.array([1.1247, -0.8540, 0.5864, 1, -0.9062, 0.9081, -0.2700])
    #X = np.array([1, 2, 3, 4, 5])
    #Y = np.array([1, 2, 3, 4, 5])
    #Y= np.array([1,2,3,4,23,1,7])
    X = np.array([-1, 0, 3, 4])
    
    Y = np.array([15.5, 3, 8, 1])
    coef = trazcuad(X, Y)
    print("Coef:\n", coef)

if __name__=="__main__":
    main()
