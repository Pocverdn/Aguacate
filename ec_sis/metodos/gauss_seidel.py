import numpy as np
import pandas as pd

def gausseidel(x0, A, b, Tol, niter, modo):
    """
    Resuelve el sistema Ax = b utilizando el método Jacobi o Gauss-Seidel (matricial).
    
    Parámetros:
    x0 (numpy.ndarray): Condición inicial
    A (numpy.ndarray): Matriz del sistema
    b (numpy.ndarray): Vector de términos independientes
    Tol (float): Tolerancia de error
    niter (int): Número máximo de iteraciones
    
    Retorna:
    s (numpy.ndarray): Solución aproximada
    E (list): Lista de errores en cada iteración
    """
    c = 0
    error = Tol + 1
    E = []  # Lista para almacenar los errores de cada iteración
    all_x = []  # Lista para almacenar los valores de x1, x2, ..., xn por iteración

    
    aux = False

    try:
    
        D = np.diag(np.diagonal(A))  # Matriz diagonal
        L = -np.tril(A, -1)           # Matriz triangular inferior
        U = -np.triu(A, 1)            # Matriz triangular superior
        
        T = np.linalg.inv(D - L) @ U
        C = np.linalg.inv(D - L) @ b

        sp_radius = max(abs(np.linalg.eigvals(T)))

    except Exception as e:
        print(f"Error en la matriz: {e}")
        return "N/A", "Error", True, 1000
    
    while error > Tol and c < niter:
        
        try:
            x1 = T @ x0 + C

            if(modo == "cs"):
                error = np.linalg.norm((x1 - x0) / x1, np.inf)
            else:
                error = np.linalg.norm(x1 - x0, np.inf)

            E.append(error)  # Error infinito
            error = E[-1]
            x0 = x1
            c += 1
            all_x.append(x1)  # Almacenar los valores de x1 en cada iteración

        except Exception as e:
            print(f"Error2: {e}")

            table_data = {'Iteración': np.arange(1, c + 1)}
    
            # Agregar las columnas para los valores de x1, x2, ..., xn
            for i in range(len(A)):
                table_data[f'x{i+1}'] = [x[i] for x in all_x]
            
            # Agregar la columna de errores
            table_data['Error'] = E
            
            # Crear el DataFrame
            df_resultado = pd.DataFrame(table_data)
            tabla_html = df_resultado.to_html(index=False, classes='table table-striped text-center')

            return tabla_html, "Error", True, sp_radius

    if error < Tol:
        s = x0
        print(f'La solución aproximada es:')
        print(s)
        print(f'\n✅ Convergió en {c} iteraciones con tolerancia {Tol}.')
    else:
        s = "Error"
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

    return tabla_html,s, aux, sp_radius