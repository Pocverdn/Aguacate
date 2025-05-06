import numpy as np

def jacobi(x0, A, b, tol, niter):
    c = 0
    error = tol + 1
    E = []
    
    D = np.diag(np.diag(A))
    L = -np.tril(A, -1)
    U = -np.triu(A, 1)
    
    T = np.linalg.inv(D).dot(L + U)
    C = np.linalg.inv(D).dot(b)
    
    while error > tol and c < niter:
        x1 = T.dot(x0) + C
        error = np.linalg.norm(x1 - x0, np.inf)
        E.append(error)
        x0 = x1
        c += 1
        print(f"Iteración {c}: x = {x0}, Error = {error}")

    if error < tol:
        print(f"\nSolución aproximada encontrada con tolerancia {tol}: {x0}")
    else:
        print(f"\nFracasó después de {niter} iteraciones.")
    
    return E, x0