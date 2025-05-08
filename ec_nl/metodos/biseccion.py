import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import base64
import io
from sympy import symbols, sympify, lambdify

pd.options.display.float_format = "{:.8f}".format

def biseccion(a, b, tol, niter, fun, Modo):
    print(a, type(a))
    print(b, type(b))
    print(tol, type(tol))
    print(fun, type(fun))

    tabla = []
    resultado = ""
    nlist = []
    xmlist = []
    res=[]
    fxmlist = []
    E = []

    x = a
    fa = fun(a)
    x = b
    fb = fun(b)

    if fa == 0:
        resultado = f"{a} es raíz de f(x)"
    elif fb == 0:
        resultado = f"{b} es raíz de f(x)"
    elif fa * fb < 0:
        i = 0
        xm = (a + b) / 2
        x = xm
        fxm = fun(x)
        xmlist.append(fxm)
        error = 100

        tabla.append([i, xm, fxm, error])

        while error > tol and fxm != 0 and i < niter:
            if fa * fxm < 0:
                b = xm
                x = b
                fb = fun(x)
            else:
                a = xm
                x = a
                fa = fun(x)

            xma = xm
            xm = (a + b) / 2
            x = xm
            fxm = fun(x)

            if (Modo == "cs"):
                error = abs((xm - xma)/xm)
            else:
                error = abs((xm - xma))
            i += 1

            tabla.append([i, xm, fxm, error])

        if fxm == 0:
            resultado = f"{x} es raíz de f(x)"
            res.append(x)
        elif error <= tol:
            resultado = f"{x} es una aproximación de una raíz con tolerancia {tol}"
        else:
            resultado = f"Fracaso en {niter} iteraciones"
    else:
        resultado = "El intervalo es inadecuado"

    df = pd.DataFrame(tabla, columns=["i", "Xm", "f(Xm)", "Error"])

    x_vals = np.linspace(a - 5, b + 5, 400)
    y_vals = [fun(x) for x in x_vals]

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {fun}', color='blue')
    plt.axhline(0, color='black', linewidth=1)
    plt.scatter(x, 0, color='red', zorder=5, label=f'Raíz: {round(x, 4)}')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Método de Punto Fijo")
    plt.legend()
    plt.grid()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode()
    img_uri = f"data:image/png;base64,{string}"

    return resultado, df.to_html(index=False, classes='table table-striped text-center'), img_uri


