import matplotlib
matplotlib.use('Agg')
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import base64
import io

def lagrange(x, y):
    n = len(x)
    tabla = np.zeros((n, n))

    for i in range(n):
        Li = np.array([1.0])
        den = 1.0
        for j in range(n):
            if j != i:
                paux = np.array([1.0, -x[j]])
                Li = np.convolve(Li, paux)
                den *= (x[i] - x[j])
        tabla[i, :len(Li)] = y[i] * Li / den

    a = np.sum(tabla, axis=0)  # coeficientes del polinomio

    # Eliminar ceros a la izquierda (por si el grado es menor a n-1)
    a = np.trim_zeros(a, 'f')
    grado = len(a) - 1

    # Construcción del string
    terms = []
    for i, coef in enumerate(a):
        power = grado - i
        if abs(coef) < 1e-10:
            continue  # Omitir términos nulos
        term = f"{coef:.4f}"
        if power > 0:
            term += f"*x^{power}" if power > 1 else "*x"
        terms.append(term)
    poly_str = " + ".join(terms).replace("+ -", "- ")

    xpol = np.linspace(min(x)-1, max(x)+1, 500)
    p = np.polyval(a, xpol)

    plt.plot(x, y, 'r*', label='Puntos dados')
    plt.plot(xpol, p, 'b-', label=f'Polinomio de grado {grado}')
    plt.title('Interpolación por Lagrange')
    plt.legend()
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('P(x)')

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode()
    img_uri = f"data:image/png;base64,{string}"

    plt.close()

    return poly_str, img_uri
