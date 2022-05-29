#!/home/salzatec1/miniconda3/bin/python
import numpy as np

def difdivididas(X, Y):
    n = X.size
    D = np.zeros((n, n)) # (shape)
    X = np.matrix.transpose(X)
    etapa = 0
    etapa += 1

    D[:,0] = np.matrix.transpose(Y)
    etapa += 1
    for i in range(1, n):
        aux0 = D[i-1:n, i-1]
        aux = np.diff(aux0)
        aux2 = X[i:n] - X[0:n-i]
        D[i:n, i] = np.divide(aux, aux2)
        etapa += 1

    print("D:\n", D)
    coef = np.diag(D)
    print("Coef:\n")
    print(coef)
    return coef

def main():
    #X = np.array([0, 2, 3, 4, 5, 6, 7])
    #
    #Y = np.array([1.1247, -0.8540, 0.5864, 1, -0.9062, 0.9081, -0.2700])
    #X = np.array([-1, 0, 3, 4])
    #
    #Y = np.array([15.5, 3, 8, 1])
    X = np.array([2, 3, 4])
    Y = np.array([1.5, 7, 2])
    coef = difdivididas(X, Y)
    print("Coef:\n", coef)

if __name__=="__main__":
    main()
