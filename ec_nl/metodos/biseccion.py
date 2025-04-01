import pandas as pd
import numpy as np
import math
from sympy import symbols, sympify, lambdify

pd.options.display.float_format = "{:.8f}".format



def biseccion(a, b, tol, niter, fun):
    print(a, type(a))
    print(b, type(b))
    print(tol, type(tol))
    print(fun, type(fun))

    tabla = []
    resultado = ""
    nlist = []
    xmlist = []
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
            error = abs(xm - xma)
            i += 1

            tabla.append([i, xm, fxm, error])

        if fxm == 0:
            resultado = f"{x} es raíz de f(x)"
        elif error <= tol:
            resultado = f"{x} es una aproximación de una raíz con tolerancia {tol}"
        else:
            resultado = f"Fracaso en {niter} iteraciones"
    else:
        resultado = "El intervalo es inadecuado"

    df = pd.DataFrame(tabla, columns=["i", "Xm", "f(Xm)", "Error"])
    return resultado, df.to_html(index=False, classes='table table-striped text-center')


