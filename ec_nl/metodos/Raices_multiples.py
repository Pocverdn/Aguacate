import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def raices_multiples(X0, Tol, Niter, Fun, df, ddf, Modo):
    tabla = []
    x = X0
    f = Fun(x)
    df_val = df(x)
    ddf_val = ddf(x)
    c = 0
    Error = 100

    tabla.append([c, x, f, Error])

    while Error > Tol and f != 0 and df_val != 0 and c < Niter:
        x_new = x - (f * df_val) / (df_val**2 - f * ddf_val)
        if (Modo == "cs"):
            Error = abs((x_new - x)/x_new)
        else:
            Error = abs(x_new - x)
        x = x_new
        f = Fun(x)
        df_val = df(x)
        ddf_val = ddf(x)
        c += 1
        tabla.append([c, x, f, Error])

    if f == 0:
        resultado = f"{x} es raíz de f(x)"
    elif Error < Tol:
        resultado = f"{x} es una aproximación de una raíz con tolerancia {Tol}"
    else:
        resultado = f"Fracaso en {Niter} iteraciones"

    df = pd.DataFrame(tabla, columns=["Iteración", "Xi", "F(Xi)", "Error"])

    x_vals = np.linspace(X0 - 5, X0 + 5, 400)
    y_vals = [eval(Fun, {"x": val, "math": math}) for val in x_vals]

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {Fun}', color='blue')
    plt.axhline(0, color='black', linewidth=1)
    plt.scatter(xn[-1], 0, color='red', zorder=5, label=f'Raíz: {round(xn[-1], 4)}')
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
