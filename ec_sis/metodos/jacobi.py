import numpy as np
import pandas as pd

def jacobi(x0, A, b, tol, niter, modo):
    c = 0
    error = tol + 1
    E = []
    all_x = []

    aux = False

    try:

        D = np.diag(np.diag(A))
        L = -np.tril(A, -1)
        U = -np.triu(A, 1)
        
        T = np.linalg.inv(D).dot(L + U)
        C = np.linalg.inv(D).dot(b)

        sp_radius = max(abs(np.linalg.eigvals(T)))

    except Exception as e:
        print(f"Error en la matriz: {e}")
        return "N/A", "Error", True, 1000
    
    while error > tol and c < niter:
        
        try:

            x1 = T.dot(x0) + C

            if(modo == "cs"):
                error = np.linalg.norm((x1 - x0) / x1, np.inf)
            else:
                error = np.linalg.norm(x1 - x0, np.inf)
                
            E.append(error)
            x0 = x1
            c += 1
            all_x.append(x1)
        except Exception as e:
            print(f"Error2: {e}")

            table_data = {'Iteración': np.arange(1, c + 1)}
            
            for i in range(len(A)):
                table_data[f'x{i+1}'] = [x[i] for x in all_x]
            
            table_data['Error'] = E
            
            df_resultado = pd.DataFrame(table_data)
            tabla_html = df_resultado.to_html(index=False, classes='table table-striped text-center')
            
            return tabla_html, "Error", True, sp_radius

    if error < tol:
        print(f"\nSolución aproximada encontrada con tolerancia {tol}: {x0}")
    else:
        x0 = "Error"
        print(f'⚠️  Fracasó en {niter} iteraciones. ')
        aux = True
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
    
    return tabla_html, x0, aux, sp_radius