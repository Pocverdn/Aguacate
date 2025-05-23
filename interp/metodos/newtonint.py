import matplotlib
matplotlib.use('Agg')
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import base64
import io

def newtonint(x, y):
    
    if len(set(x)) != len(x):
        xpol = np.linspace(min(x)-1, max(x)+1, 500)

        plt.plot(x, y, 'r*', label='Puntos dados')
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

        return "Error", img_uri
    
    if len(x) != len(y):
        xpol = np.linspace(min(x)-1, max(x)+1, 500)

        plt.plot(x, y, 'r*', label='Puntos dados')
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

        return "Error", img_uri

    try:
        n = len(x)
        x = np.array(x, dtype=float)
        y = np.array(y, dtype=float)

        # Tabla de diferencias divididas
        tabla = np.zeros((n, n))
        tabla[:, 0] = y
        for j in range(1, n):
            for i in range(j, n):
                tabla[i, j] = (tabla[i, j-1] - tabla[i-1, j-1]) / (x[i] - x[i-j])

        # Coeficientes de la forma de Newton
        coef_newton = tabla[np.arange(n), np.arange(n)]

        # Convertir a forma estándar (coeficientes para np.polyval)
        poly_std = np.array([0.])
        base = np.array([1.])

        for i in range(n):
            term = coef_newton[i] * base
            poly_std = np.pad(poly_std, (len(term) - len(poly_std), 0), 'constant')
            term = np.pad(term, (len(poly_std) - len(term), 0), 'constant')
            poly_std = poly_std + term
            base = np.convolve(base, [1, -x[i]])  # (x - x_i)

        a = poly_std  # Coeficientes del polinomio en forma estándar
        grado = len(a) - 1
    except Exception as e:
        print(f"Error en la matriz: {e}")
        xpol = np.linspace(min(x)-1, max(x)+1, 500)

        plt.plot(x, y, 'r*', label='Puntos dados')
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

        return "Error", img_uri

    # Construir string del polinomio
    terms = []
    for i, coef in enumerate(a):
        try:

            power = grado - i
            if abs(coef) < 1e-10:
                continue
            term = f"{coef:.4f}"
            if power > 0:
                term += f"*x^{power}" if power > 1 else "*x"
            terms.append(term)
        except Exception as e:
            print(f"Error en la matriz: {e}")

            xpol = np.linspace(min(x)-1, max(x)+1, 500)

            plt.plot(x, y, 'r*', label='Puntos dados')
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

            return "Error", img_uri

    poly_str = " + ".join(terms).replace("+ -", "- ")

    xpol = np.linspace(min(x)-1, max(x)+1, 500)
    p = np.polyval(a, xpol)

    plt.plot(x, y, 'ro', label='Puntos dados')
    plt.plot(xpol, p, 'b-', label=f'Polinomio de grado {grado}')
    plt.title('Interpolación por diferencias divididas de Newton')
    plt.xlabel('x')
    plt.ylabel('P(x)')
    plt.grid(True)
    plt.legend()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode()
    img_uri = f"data:image/png;base64,{string}"

    plt.close()

    return poly_str, img_uri

