from IPython.display import display, Math
import numpy as np
from itertools import combinations

def ecuacionGeneral(p, v, u):
    a, b, c = p #destructuring
    display(
        Math(
            rf"""
            0 = {v[1]*u[2] - v[2]*u[1]}x + {v[2]*u[0] - v[0]*u[2]}y + {v[0]*u[1] - v[1]*u[0]}z + {
            -a*v[1]*u[2] - b*v[2]*u[0] - c*v[0]*u[1] + a*v[2]*u[1] + b*v[0]*u[2] + c*v[1]*u[0]
            }
            """
        )
    )

def compararVectoresDirectores(v, u):
    equal = True
    proportion = ""

    for i in range(0, v.shape[0]):
        # Evitamos tratar de dividir entre 0
        if(v[i] == 0):
            if (u[i] == 0):
                equal = True
            else:
                equal = False
        else:
            if (proportion == ""):
                proportion = v[i] / u[i]
            else:
                if(proportion == v[i] / u[i]):   
                    equal = True
                else:
                    equal = False

    return equal

def onePointInLine(a, c, d):
    v = d-c

    pointInLine = True
    lambdaValue = ""
    for idx in range(v.shape[0]):
        if v[idx] != 0:
            lambdaValue = (a[idx] - c[idx]) / v[idx]
            break

    else:
        return np.allclose(a, c) # si se da el raro caso de que son el mismo punto. a == c == d

    
    for i in range(1, a.shape[0]):
        if v[i] == 0:
            if a[i] != c[i]:
                pointInLine = False
        else:        
            # ambas expresiones son válidas, pero es mejor usar la segunda para evitar las diferencias de redondeo.
            # if (lambdaValue != (a[i] - c[i]) / v[i]):
            if not np.isclose((a[i] - c[i]) / v[i], lambdaValue):
                pointInLine = False
    
    return pointInLine

def typeVectorPair(a , b, c, d):
    v = b - a
    u = d - c

    if (compararVectoresDirectores(v, u)):
        if (onePointInLine(a, c, d)): # si las rectas son coincindentes
            print("Se trata de dos rectas coincidentes.")
        else:
            print("Se tratan de dos rectas paralelas no coincidentes.")
    else:
        # thirdVector = newVector(v, u) # A partir de los vectores v y u creamos un nuevo vector que contienen los puntos finales.
        thirdVector = d - b
        M = np.array([v, u, thirdVector])
        matrix = M.T #Nos interesa ver los vectores como las columnas de la matriz.
        print(matrix)
        if (np.linalg.det(matrix) == 0): # el determinante de la matriz con esos dos y un tercero formado por puntos de los dos.
            if (np.dot(v, u) == 0): # Hacemos el producto escalar de los dos vectores.
                print("Se tratan de dos rectas perpendiculares.")
            else:
                print("Se trata de dos rectas secantes.")
        else:
            print("Rectes que es creuen.") 

def forma_escalonada(matriz):
    A = matriz.astype(float).copy()
    filas, columnas = A.shape
    fila_pivote = 0

    for col in range(columnas):
        if fila_pivote >= filas:
            break

        max_fila = np.argmax(np.abs(A[fila_pivote:, col])) + fila_pivote
        if A[max_fila, col]  == 0:
            continue

        A[[fila_pivote, max_fila]] = A[[max_fila, fila_pivote]]

        A[fila_pivote] = A[fila_pivote] / A[fila_pivote, col]

        for f in range(fila_pivote + 1, filas):
            A[f] = A[f] - A[fila_pivote] * A[f, col]

        fila_pivote += 1

    return A

def adjunta(matriz):
    A = np.array(matriz, dtype=float)
    n, m = A.shape

    if n != m:
        raise ValueError("La matriz debe ser cuadrada para calcular la adjunta.")

    adj = np.zeros_like(A)

    for i in range(n):
        for j in range(n):
            menor = np.delete(np.delete(A, i, axis=0), j, axis=1)

            cofactor = ((-1) ** (i + j)) * np.linalg.det(menor)
            adj[j, i] = cofactor

    return adj

def cofactores(matriz):
    A = np.array(matriz, dtype=float)
    n, m = A.shape

    if n != m:
        raise ValueError("La matriz debe ser cuadrada para calcular la adjunta.")

    adj = np.zeros_like(A)

    for i in range(n):
        for j in range(n):
            menor = np.delete(np.delete(A, i, axis=0), j, axis=1)

            cofactor = ((-1) ** (i + j)) * np.linalg.det(menor)
            adj[i,j] = cofactor

    return adj

def trasposicionManual(matrix):
    g = matrix.copy()

    a = np.empty(matrix.shape)


    n, m = g.shape

    for i in range(n):
        for j in range(m):
            a[j, i] = g[i, j]

    return a
    

def ValorKDet0(M, kIni, kFin):
    KValues = []
    vector.reshape(M.shape) 
    for k in range(kIni, kFin):
        filas = M.shape[0]
        columnas = M.shape[1]
        vector = np.array([])
        for i in range(filas):
            for j in range(columnas):
                np.append(vector, M[i][j])
        if np.linalg.det(A) == 0:
            KValues.append(k)
    return KValues


def MinorDetDif0(M, eye, verbose = True):
    filas, columnas = M.shape

    filas_combi = list(combinations(range(filas), eye))
    col_combi = list(combinations(range(columnas), eye))

    for f_idxs in filas_combi:
        for c_idxs in col_combi:
            submatriz = M[np.ix_(f_idxs, c_idxs)]
            det = np.linalg.det(submatriz)
            if verbose:
                print(f"Filas {f_idxs}, Columnas {c_idxs}")
                print(submatriz)
                print(f"Det: {det:.2f}\n")
            if (det):
                return True
    
    return False
    
def RangeOfMatrix(M ,n, verbose = True):
    
    if MinorDetDif0(M, n, verbose):
        return n
    else:
        return RangeOfMatrix(M, n - 1, verbose)
    
    

print("Ejecutado")
