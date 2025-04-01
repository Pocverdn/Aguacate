import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
import io
import base64


def metodo_newton(X0, Tol, Niter, Fun, df_expr):
    fn = []
    xn = []
    E = []
    N = []
    x = X0
    f = eval(Fun, {"x": x, "math": math})
    derivada = eval(df_expr, {"x": x, "math": math})
    c = 0
    Error = 100               
    fn.append(f)
    xn.append(x)
    E.append(Error)
    N.append(c)

    tabla = []
    tabla.append([c, x, f, Error])

    while Error > Tol and f != 0 and derivada != 0 and c < Niter:
        x = x - f / derivada
        derivada = eval(df_expr, {"x": x, "math": math})
        f = eval(Fun, {"x": x, "math": math})
        fn.append(f)
        xn.append(x)
        c += 1
        Error = abs(xn[c] - xn[c - 1])
        N.append(c)
        E.append(Error)
        tabla.append([c, x, f, Error])

    if f == 0:
        resultado = f"{x} es raíz de f(x)"
    elif Error < Tol:
        resultado = f"{x} es una aproximación de una raíz de f(x) con tolerancia {Tol}"
    else:
        resultado = f"Fracaso en {Niter} iteraciones"

    df_resultado = pd.DataFrame(tabla, columns=["I", "Xi", "F(Xi)", "E"])
    tabla_html = df_resultado.to_html(index=False, classes='table table-striped text-center')

    x_vals = np.linspace(min(xn) - 1, max(xn) + 1, 100)
    y_vals = [eval(Fun, {"x": val, "math": math}) for val in x_vals]

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {Fun}', color='blue')
    plt.axhline(0, color='black', linewidth=1)
    plt.scatter(xn[-1], 0, color='red', zorder=5, label=f'Raíz: {round(xn[-1], 4)}')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Método de Newton")
    plt.legend()
    plt.grid()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode()
    img_uri = f"data:image/png;base64,{string}"

    return resultado, tabla_html, img_uri


def metodo_newtonCS(X0, Tol, Niter, Fun, df_expr):
    fn = []
    xn = []
    E = []
    e = []
    N = []

    try:
        f_lambda = lambda x: eval(Fun, {"x": x, "math": math})
        df_lambda = lambda x: eval(df_expr, {"x": x, "math": math})
    except Exception as ex:
        return f"Error en la evaluación de la función: {ex}", "", ""

    x = X0
    f = f_lambda(x)
    derivada = df_lambda(x)
    
    if derivada == 0:
        return "La derivada es cero en el punto inicial, no se puede aplicar el método de Newton.", "", ""

    c = 0
    error = 100

    fn.append(f)
    xn.append(x)
    E.append(error)
    e.append(error)
    N.append(c)

    tabla = [[c, x, f, error]]

    while error > Tol and abs(f) > Tol and c < Niter:
        try:
            x_new = x - f / derivada
        except ZeroDivisionError:
            return "Error: división por cero al calcular x_new", "", ""
        
        derivada = df_lambda(x_new)
        f = f_lambda(x_new)

        Error = abs(x_new - x)
        error = Error / abs(x_new) if x_new != 0 else Error

        c += 1
        fn.append(f)
        xn.append(x_new)
        N.append(c)
        E.append(Error)
        e.append(error)
        tabla.append([c, x_new, f, error])

        x = x_new
    
    if abs(f) <= Tol:
        resultado = f"{x} es una raíz de f(x) con tolerancia {Tol}"
    elif error < Tol:
        resultado = f"{x} es una aproximación de una raíz de f(x) con tolerancia {Tol}"
    else:
        resultado = f"Fracaso en {Niter} iteraciones"

    df_resultado = pd.DataFrame(tabla, columns=["Iteración", "Xi", "F(Xi)", "Error relativo"])
    tabla_html = df_resultado.to_html(index=False, classes='table table-striped text-center')

    x_vals = np.linspace(min(xn) - 1, max(xn) + 1, 100)
    y_vals = [f_lambda(val) for val in x_vals]

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {Fun}', color='blue')
    plt.axhline(0, color='black', linewidth=1)
    plt.scatter(xn[-1], 0, color='red', zorder=5, label=f'Raíz: {round(xn[-1], 4)}')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Método de Newton")
    plt.legend()
    plt.grid()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode()
    img_uri = f"data:image/png;base64,{string}"

    return resultado, tabla_html, img_uri
