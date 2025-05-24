import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def spline_cubico(x, y):

    if len(set(x)) != len(x):

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
        A = np.zeros((4*(n-1), 4*(n-1)))
        b = np.zeros(4*(n-1))

        c = 0
        h = 0
        for i in range(n - 1):
            A[h, c] = x[i]**3
            A[h, c+1] = x[i]**2
            A[h, c+2] = x[i]
            A[h, c+3] = 1
            b[h] = y[i]
            c += 4
            h += 1

        c = 0
        for i in range(1, n):
            A[h, c] = x[i]**3
            A[h, c+1] = x[i]**2
            A[h, c+2] = x[i]
            A[h, c+3] = 1
            b[h] = y[i]
            c += 4
            h += 1

        c = 0
        for i in range(1, n - 1):
            A[h, c] = 3*x[i]**2
            A[h, c+1] = 2*x[i]
            A[h, c+2] = 1
            A[h, c+4] = -3*x[i]**2
            A[h, c+5] = -2*x[i]
            A[h, c+6] = -1
            b[h] = 0
            c += 4
            h += 1

        c = 0
        for i in range(1, n - 1):
            A[h, c] = 6*x[i]
            A[h, c+1] = 2
            A[h, c+4] = -6*x[i]
            A[h, c+5] = -2
            b[h] = 0
            c += 4
            h += 1

        A[h, 0] = 6 * x[0]
        A[h, 1] = 2
        b[h] = 0
        h += 1

        A[h, -4] = 6 * x[-1]
        A[h, -3] = 2
        b[h] = 0

        coef = np.linalg.solve(A, b)
        tabla = coef.reshape((n-1, 4))
        poly_str, polinomios = obtener_poly_cub_str(x, tabla)
    except Exception as e:
        print(f"Error en la matriz: {e}")

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
    
    grafica  = graficar_cubico(x,y,tabla)
    return poly_str, grafica, polinomios

def obtener_poly_cub_str(x, tabla):
    n_tramos = len(tabla)
    polinomios_str = []
    polinomios = []

    for i in range(n_tramos):
        a, b, c, d = tabla[i]
        tramo = f"{x[i]} ≤ x ≤ {x[i+1]}"
        pol = (f"{a:.4f}*x**3 + {b:.4f}*x**2 + {c:.4f}*x + {d:.4f}")
        polinomios_str.append(f"Tramo {i+1} ({tramo}):  y = {pol}")
        polinomios.append(pol)

    return polinomios_str, polinomios

def graficar_cubico(x, y, tabla):
    plt.plot(x, y, 'r*', label='Puntos de datos')
    for i in range(len(tabla)):
        x_vals = np.linspace(x[i], x[i+1], 200)
        y_vals = (tabla[i, 0]*x_vals**3 + tabla[i, 1]*x_vals**2 +
                  tabla[i, 2]*x_vals + tabla[i, 3])
        plt.plot(x_vals, y_vals, label=f'Tramo {i+1}')
    plt.title("Spline Cúbico")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode()
    img_uri = f"data:image/png;base64,{string}"
    plt.close()

    return img_uri
