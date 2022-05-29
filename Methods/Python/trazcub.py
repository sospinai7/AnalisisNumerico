#!/home/salzatec1/miniconda3/bin/python
import numpy as np
from gausstot import gausstot
from gausspl import gausspl

def trazcub(X, Y):
    n = X.size
    m = 4*(n-1)
    A = np.zeros((m, m)) # (shape)
    b = np.zeros(m)
    coef = np.zeros((n-1, 4))
    print(A)

    # Condiciones de interpolacion
    for i in range(n - 1):
        A[i+1, 4*i:4*i+4] = np.array([X[i+1]**3, X[i+1]**2, X[i+1], 1])
        b[i+1] = Y[i+1]

    A[0, 0:4] = np.array([X[0]**3, X[0]**2, X[0], 1])
    b[0] = Y[0]

    # Condiciones de continuidad
    for i in range(1, n-1):
        A[n+i-1, 4*i-4:4*i+4] = np.array([X[i]**3, X[i]**2, X[i], 1, -X[i]**3, -X[i]**2, -X[i], -1])
        b[n+i-1] = 0

    # Condiciones de suavidad
    for i in range(1, n-1):
        A[2*n+i-4, 4*i-4:4*i+4] = np.array([3*X[i]**2, 2*X[i], 1, 0, -3*X[i]**2, -2*X[i], -1, 0])
        b[2*n+i-4] = 0

    # Condiciones de concavidad - TODO
    for i in range(1, n-1):
        A[3*n+i-4, 4*i-4:4*i+4] = np.array([3*X[i]**2, 2*X[i], 1, 0, -3*X[i]**2, -2*X[i], -1, 0])
        b[2*n+i-4] = 0

    # Condiciones de frontera - TODO
    for i in range(1, n-1):
        A[2*n+i-4, 4*i-4:4*i+4] = np.array([3*X[i]**2, 2*X[i], 1, 0, -3*X[i]**2, -2*X[i], -1, 0])
        b[2*n+i-4] = 0

    A[m-1, 0] = 2
    b[m-1] = 0
    # Hasta aqui todo va bien

    Saux = gausstot(A, b)

    for i in range(n-1):
        coef[i,:] = Saux[4*i:4*i+4]
    return coef

def main():
    #np.set_printoptions(suppress=True)
    X = np.array([1, 2, 3])
    Y = np.array([1.1247, -0.8540, 0.5864])
    #X = np.array([1, 2, 3, 4, 5])
    #Y = np.array([1, 2, 3, 4, 5])
    #Y= np.array([1,2,3,4,23,1,7])
    coef = trazcub(X, Y)
    print("Coef:\n", coef)

if __name__=="__main__":
    main()
