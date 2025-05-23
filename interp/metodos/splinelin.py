import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def spline_lineal(x, y):

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
        A = np.zeros((2*(n-1), 2*(n-1)))
        b = np.zeros(2*(n-1))

        c = 0
        h = 0
        for i in range(n - 1):
            A[h, c] = x[i]
            A[h, c+1] = 1
            b[h] = y[i]
            c += 2
            h += 1

        c = 0
        for i in range(1, n):
            A[h, c] = x[i]
            A[h, c+1] = 1
            b[h] = y[i]
            c += 2
            h += 1

        coef = np.linalg.solve(A, b)
        tabla = coef.reshape((n-1, 2))
        poly_str = obtener_poli_str(x, tabla)
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
    
   

    grafica  = graficar_lineal(x,y,tabla)
    return poly_str, grafica

def obtener_poli_str(x, tabla):
    n_tramos = len(tabla)
    polinomios_str = []

    for i in range(n_tramos):
        m, b = tabla[i]
        tramo = f"{x[i]} ≤ x ≤ {x[i+1]}"
        pol = f"{m:.4f}·x + {b:.4f}"
        polinomios_str.append(f"Tramo {i+1} ({tramo}):  y = {pol}")

    return polinomios_str

def graficar_lineal(x, y, tabla):
    plt.plot(x, y, 'r*', label='Puntos de datos')
    for i in range(len(tabla)):
        x_vals = np.linspace(x[i], x[i+1], 200)
        y_vals = tabla[i, 0] * x_vals + tabla[i, 1]
        plt.plot(x_vals, y_vals, label=f'Tramo {i+1}')
    plt.title("Spline Lineal")
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