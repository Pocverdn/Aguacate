import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

def raices_multiples(X0, Tol, Niter, Fun, df, ddf, Modo):
    tabla = []
    x = X0

    try:
        f = eval(Fun, {"x": x, "math": math})
        df_val = eval(df, {"x": x, "math": math})
        ddf_val = eval(ddf, {"x": x, "math": math})
        c = 0
        Error = 100

        tabla.append([c, x, f, Error])

    except Exception as e:
        print(f"1: {e}")

        tabla = [[0, 0, 0, 0]]

        df = pd.DataFrame(tabla, columns=["Iteración", "Xi", "F(Xi)", "Error"])

        x_vals = np.linspace(X0 - 5, X0 + 5, 400)
        y_vals = [eval(Fun, {"x": val, "math": math}) for val in x_vals]

        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label=f'f(x) = {Fun}', color='blue')
        plt.axhline(0, color='black', linewidth=1)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Método de Raíces Múltiples")
        plt.legend()
        plt.grid()

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        string = base64.b64encode(buf.read()).decode()
        img_uri = f"data:image/png;base64,{string}"

        resultado = "Error"

        return resultado, df.to_html(index=False, classes='table table-striped text-center'), img_uri

    while Error > Tol and f != 0 and df_val != 0 and c < Niter:
        
        try:
            x_new = x - (f * df_val) / (df_val**2 - f * ddf_val)
            if (Modo == "cs"):
                Error = abs((x_new - x)/x_new)
            else:
                Error = abs(x_new - x)
            x = x_new
            f = eval(Fun, {"x": x, "math": math})
            df_val = eval(df, {"x": x, "math": math})
            ddf_val = eval(ddf, {"x": x, "math": math})
            c += 1
            tabla.append([c, x, f, Error])
        except Exception as e:
            print(f"2: {e}")

            df = pd.DataFrame(tabla, columns=["Iteración", "Xi", "F(Xi)", "Error"])

            x_vals = np.linspace(X0 - 5, X0 + 5, 400)
            y_vals = [eval(Fun, {"x": val, "math": math}) for val in x_vals]

            plt.figure(figsize=(8, 6))
            plt.plot(x_vals, y_vals, label=f'f(x) = {Fun}', color='blue')
            plt.axhline(0, color='black', linewidth=1)
            plt.xlabel("x")
            plt.ylabel("f(x)")
            plt.title("Método de Raíces Múltiples")
            plt.legend()
            plt.grid()

            buf = io.BytesIO()
            plt.savefig(buf, format="png")
            buf.seek(0)
            string = base64.b64encode(buf.read()).decode()
            img_uri = f"data:image/png;base64,{string}"

            resultado = "Error"

            return resultado, df.to_html(index=False, classes='table table-striped text-center'), img_uri
            

    if f == 0:
        resultado = f"{x} es raíz de f(x)"
    elif Error < Tol:
        resultado = f"{x} es una aproximación de una raíz con tolerancia {Tol}"
    else:
        df = pd.DataFrame(tabla, columns=["Iteración", "Xi", "F(Xi)", "Error"])

        x_vals = np.linspace(X0 - 5, X0 + 5, 400)
        y_vals = [eval(Fun, {"x": val, "math": math}) for val in x_vals]

        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label=f'f(x) = {Fun}', color='blue')
        plt.axhline(0, color='black', linewidth=1)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Método de Raíces Múltiples")
        plt.legend()
        plt.grid()

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        string = base64.b64encode(buf.read()).decode()
        img_uri = f"data:image/png;base64,{string}"

        resultado = f'Error en la iteracion {Niter}, ultima aproximacion: {x}'

        return resultado, df.to_html(index=False, classes='table table-striped text-center'), img_uri

    df = pd.DataFrame(tabla, columns=["Iteración", "Xi", "F(Xi)", "Error"])

    x_vals = np.linspace(X0 - 5, X0 + 5, 400)
    y_vals = [eval(Fun, {"x": val, "math": math}) for val in x_vals]

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {Fun}', color='blue')
    plt.axhline(0, color='black', linewidth=1)
    plt.scatter(x, 0, color='red', zorder=5, label=f'Raíz: {round(x, 4)}')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Método de Raíces Múltiples")
    plt.legend()
    plt.grid()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode()
    img_uri = f"data:image/png;base64,{string}"

    return resultado, df.to_html(index=False, classes='table table-striped text-center'), img_uri
