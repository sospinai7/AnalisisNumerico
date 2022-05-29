import numpy as np

def sustreg(M):
    n = M.shape[0]
    # Creamos el vector solucion con numero de filas de M inicializado en 0
    x = np.zeros(n)
    if np.iscomplexobj(M):
        x = x.astype(complex)
    # Sacamos el primer valor del vector solucion
    x[n-1] = M[n-1][n]/M[n-1][n-1]
    # Iteramos por cada fila utilizando valores anteriores del vector solucion
    for i in range(n-1, -1, -1):
        aux = np.hstack((1, x[i+1:n]))
        aux1 = np.hstack((M[i][n], -M[i][i+1:n]))
        x[i] = np.dot(aux, aux1)/M[i][i]
    return x
