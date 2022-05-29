import numpy as np

def sustprog(M):
    n = M.shape[0]
    # Creamos el vector solucion con numero de filas de M inicializado en 0
    x = np.zeros(n)
    if np.iscomplexobj(M):
        x = x.astype(complex)
    # Sacamos el primer valor del vector solucion
    x[0] = M[0][n]/M[0][0]
    # Iteramos por cada fila utilizando valores anteriores del vector solucion
    for i in range(1, n):
        aux = np.hstack((1, np.matrix.transpose(x[0:i])))
        aux1 = np.hstack((M[i][n], - M[i, 0:i]))
        x[i] = np.dot(aux, aux1)/M[i][i]
    return x
