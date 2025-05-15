import numpy as np
import pandas as pd

def jacobi(x0, A, b, tol, niter):
    c = 0
    error = tol + 1
    E = []
    all_x = []
    
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
        all_x.append(x1)

    if error < tol:
        print(f"\nSolución aproximada encontrada con tolerancia {tol}: {x0}")
    else:
        print(f"\nFracasó después de {niter} iteraciones.")

    # Crear la tabla con pandas
    table_data = {'Iteración': np.arange(1, c + 1)}
    
    # Agregar las columnas para los valores de x1, x2, ..., xn
    for i in range(len(A)):
        table_data[f'x{i+1}'] = [x[i] for x in all_x]
    
    # Agregar la columna de errores
    table_data['Error'] = E
    
    # Crear el DataFrame
    df_resultado = pd.DataFrame(table_data)
    tabla_html = df_resultado.to_html(index=False, classes='table table-striped text-center')
    
    return tabla_html, x0