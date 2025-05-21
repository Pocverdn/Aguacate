import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import base64
import io

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


    try:
        x = a
        fa = eval(fun, {"x": a, "math": math})
        x = b
        fb = eval(fun, {"x": b, "math": math})

    except Exception as e:
        print(f"1: {e}")

        tabla = [[0, 0, 0, 0]]

        df = pd.DataFrame(tabla, columns=["i", "Xm", "f(Xm)", "Error"])

        x_vals = np.linspace(a - 5, b + 5, 400)
        y_vals = [eval(fun, {"x": x, "math": math}) for x in x_vals]

        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label=f'f(x) = {str(fun)}', color='blue')
        plt.axhline(0, color='black', linewidth=1)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Método de Bisección")
        plt.legend()
        plt.grid()

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        string = base64.b64encode(buf.read()).decode()
        img_uri = f"data:image/png;base64,{string}"

        resultado = "Error"

        return resultado, df.to_html(index=False, classes='table table-striped text-center'), img_uri



    if fa * fb < 0:
        i = 0
        xm = (a + b) / 2
        x = xm
        fxm = fb = eval(fun, {"x": x, "math": math})
        xmlist.append(fxm)
        error = 100

        tabla.append([i, xm, fxm, error])

        while error > tol and fxm != 0 and i < niter:

            try:
                if fa * fxm < 0:
                    b = xm
                    x = b
                    eval(fun, {"x": x, "math": math})
                else:
                    a = xm
                    x = a
                    fa = fb = eval(fun, {"x": x, "math": math})

                xma = xm
                xm = (a + b) / 2
                x = xm
                fxm = eval(fun, {"x": x, "math": math})

                if (Modo == "cs"):
                    error = abs((xm - xma)/xm)
                else:
                    error = abs((xm - xma))
                i += 1

                tabla.append([i, xm, fxm, error])

            except Exception as e:
                print(f"2: {e}")
                df = pd.DataFrame(tabla, columns=["i", "Xm", "f(Xm)", "Error"])

                x_vals = np.linspace(a - 5, b + 5, 400)
                y_vals = [eval(fun, {"x": x, "math": math}) for x in x_vals]

                plt.figure(figsize=(8, 6))
                plt.plot(x_vals, y_vals, label=f'f(x) = {str(fun)}', color='blue')
                plt.axhline(0, color='black', linewidth=1)
                plt.scatter(x, 0, color='red', zorder=5, label=f'Raíz: {round(x, 4)}')
                plt.xlabel("x")
                plt.ylabel("f(x)")
                plt.title("Método de Bisección")
                plt.legend()
                plt.grid()

                buf = io.BytesIO()
                plt.savefig(buf, format="png")
                buf.seek(0)
                string = base64.b64encode(buf.read()).decode()
                img_uri = f"data:image/png;base64,{string}"

                resultado = f'Error'

                return resultado, df.to_html(index=False, classes='table table-striped text-center'), img_uri

        if fxm == 0:
            resultado = f"{x} es raíz de f(x)"
            res.append(x)
        elif error <= tol:
            resultado = f"{x} es una aproximación de una raíz con tolerancia {tol}"
        else:
            df = pd.DataFrame(tabla, columns=["i", "Xm", "f(Xm)", "Error"])

            x_vals = np.linspace(a - 5, b + 5, 400)
            y_vals = [eval(fun, {"x": x, "math": math}) for x in x_vals]

            plt.figure(figsize=(8, 6))
            plt.plot(x_vals, y_vals, label=f'f(x) = {str(fun)}', color='blue')
            plt.axhline(0, color='black', linewidth=1)
            plt.scatter(x, 0, color='red', zorder=5, label=f'Raíz: {round(x, 4)}')
            plt.xlabel("x")
            plt.ylabel("f(x)")
            plt.title("Método de Bisección")
            plt.legend()
            plt.grid()

            buf = io.BytesIO()
            plt.savefig(buf, format="png")
            buf.seek(0)
            string = base64.b64encode(buf.read()).decode()
            img_uri = f"data:image/png;base64,{string}"

            resultado = f'Error en la iteracion {niter}, ultima aproximacion: {x}'

            return resultado, df.to_html(index=False, classes='table table-striped text-center'), img_uri

    elif fa == 0:
        resultado = f"{a} es raíz de f(x)"
    elif fb == 0:
        resultado = f"{b} es raíz de f(x)"
    else:
        df = pd.DataFrame(tabla, columns=["i", "Xm", "f(Xm)", "Error"])

        x_vals = np.linspace(a - 5, b + 5, 400)
        y_vals = [eval(fun, {"x": x, "math": math}) for x in x_vals]

        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label=f'f(x) = {str(fun)}', color='blue')
        plt.axhline(0, color='black', linewidth=1)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Método de Bisección")
        plt.legend()
        plt.grid()

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        string = base64.b64encode(buf.read()).decode()
        img_uri = f"data:image/png;base64,{string}"

        resultado = "Error"

        return resultado, df.to_html(index=False, classes='table table-striped text-center'), img_uri

    

    df = pd.DataFrame(tabla, columns=["i", "Xm", "f(Xm)", "Error"])

    x_vals = np.linspace(a - 5, b + 5, 400)
    y_vals = [eval(fun, {"x": x, "math": math}) for x in x_vals]

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {str(fun)}', color='blue')
    plt.axhline(0, color='black', linewidth=1)
    plt.scatter(x, 0, color='red', zorder=5, label=f'Raíz: {round(x, 4)}')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Método de Bisección")
    plt.legend()
    plt.grid()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode()
    img_uri = f"data:image/png;base64,{string}"

    return resultado, df.to_html(index=False, classes='table table-striped text-center'), img_uri


