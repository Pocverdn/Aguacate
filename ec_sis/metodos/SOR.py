import numpy as np
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import base64
import io
from sympy import symbols, sympify, lambdify

import numpy as np
import pandas as pd

def SOR(x0, A, b, Tol, niter, w, Modo="abs"):
    """
    Método de Gauss-Seidel relajado (SOR).
    
    Parámetros:
    x0 (numpy.ndarray): Vector inicial.
    A (numpy.ndarray): Matriz de coeficientes.
    b (numpy.ndarray): Vector del lado derecho.
    Tol (float): Tolerancia de convergencia.
    niter (int): Número máximo de iteraciones.
    w (float): Parámetro de relajación.
    Modo (str): "cs" para error relativo, otro valor para error absoluto.

    Retorna:
    tabla_html (str): Tabla de iteraciones en formato HTML.
    s (numpy.ndarray): Solución aproximada.
    E (list): Lista de errores en cada iteración.
    """
    c = 0
    error = Tol + 1
    E = []        # Lista de errores por iteración
    all_x = []    # Lista de vectores de solución por iteración

    aux = False

    try:

        D = np.diag(np.diag(A))
        L = -np.tril(A, -1)
        U = -np.triu(A, 1)

    except Exception as e:
        print(f"Error en la matriz: {e}")
        return "N/A", "Error", True, "N/A"

    while error > Tol and c < niter:
        
        try:

            T = np.linalg.inv(D - w * L) @ ((1 - w) * D + w * U)
            C = w * np.linalg.inv(D - w * L) @ b
            x1 = T @ x0 + C

            sp_radius = max(abs(np.linalg.eigvals(T)))

            # Cálculo del error
            if Modo == "cs":
                error = np.linalg.norm((x1 - x0) / x1, ord=np.inf)
            else:
                error = np.linalg.norm(x1 - x0, ord=np.inf)

            E.append(error)
            all_x.append(x1.copy())
            x0 = x1
            c += 1

        except Exception as e:
            print(f"Error2: {e}")

            table_data = {'Iteración': np.arange(1, c + 1)}
            for i in range(len(A)):
                table_data[f'x{i+1}'] = [x[i] for x in all_x]
            table_data['Error'] = E

            df_resultado = pd.DataFrame(table_data)
            tabla_html = df_resultado.to_html(index=False, classes='table table-striped text-center')

            return tabla_html, "Error", True, sp_radius

    s = x0

    if error < Tol:
        print(f'\n✅ Convergió en {c} iteraciones con tolerancia {Tol}.')
        print("Solución aproximada:")
        print(s)
    else:
        print(f'\n⚠️  Fracasó en {niter} iteraciones.')
        s = "Error"
        aux = True

    # Crear DataFrame para la tabla
    table_data = {'Iteración': np.arange(1, c + 1)}
    for i in range(len(A)):
        table_data[f'x{i+1}'] = [x[i] for x in all_x]
    table_data['Error'] = E

    df_resultado = pd.DataFrame(table_data)
    tabla_html = df_resultado.to_html(index=False, classes='table table-striped text-center')

    return tabla_html, s, aux, sp_radius
