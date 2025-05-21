import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
import io
import urllib, base64


pd.options.display.float_format = "{:.16f}".format

def punto_fijo(X0, Tol, Niter, Fun, g):
    fn = []
    xn = []
    E = []
    N = []
    x = X0
    f = eval(Fun, {"x": x, "math": math})
    
    try:
        c = 0
        Error = 100
        fn.append(f)
        xn.append(x)
        E.append(Error)
        N.append(c)
        tabla = []
        tabla.append([c, x, f, Error])
    except Exception as e:
        print(f"1: {e}")

        tabla = [[0, 0, 0, 0]]

        df = pd.DataFrame(tabla, columns=["I", "Xi", "F(Xi)", "E"])

        x_vals = np.linspace(X0 - 5, X0 + 5, 400) 
        y_vals = [eval(Fun, {"x": val, "math": math}) for val in x_vals] 

        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label=f'f(x) = {Fun}', color='blue')
        plt.axhline(0, color='black', linewidth=1)  
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

        resultado = "Error"

        return resultado, df.to_html(index=False, classes='table table-striped text-center'), img_uri


    while Error > Tol and f != 0 and c < Niter:

        try:
            x = eval(g, {"x": x, "math": math})
            fe = eval(Fun, {"x": x, "math": math})
            fn.append(fe)
            xn.append(x)
            c += 1
            Error = abs(xn[c] - xn[c - 1])
            N.append(c)
            E.append(Error)
            tabla.append([c, x, fe, Error])
            f = fe
        except Exception as e:
            print(f"2: {e}")

            df = pd.DataFrame(tabla, columns=["I", "Xi", "F(Xi)", "E"])

            x_vals = np.linspace(X0 - 5, X0 + 5, 400) 
            y_vals = [eval(Fun, {"x": val, "math": math}) for val in x_vals] 

            plt.figure(figsize=(8, 6))
            plt.plot(x_vals, y_vals, label=f'f(x) = {Fun}', color='blue')
            plt.axhline(0, color='black', linewidth=1)  
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

            resultado = "Error"

            return resultado, df.to_html(index=False, classes='table table-striped text-center'), img_uri


    resultado = ""
    if f == 0:
        resultado = f"{x} es raíz de f(x)"
    elif Error < Tol:
        resultado = f"{x} es una aproximación de una raíz de f(x) con tolerancia {Tol}"
    else:
        df = pd.DataFrame(tabla, columns=["I", "Xi", "F(Xi)", "E"])

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

        resultado = f'Error en la iteracion {Niter}, ultima aproximacion: {x}'

        return resultado, df.to_html(index=False, classes='table table-striped text-center'), img_uri



    df = pd.DataFrame(tabla, columns=["I", "Xi", "F(Xi)", "E"])


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




def punto_fijoCS(X0, Tol, Niter, Fun, g):
    fn = []
    xn = []
    E = []
    e = []
    N = []

    x = X0
    f = eval(Fun, {"x": x, "math": math})  

    try:
        c = 0
        Error = 100
        error = 100

        fn.append(f)
        xn.append(x)
        E.append(Error)
        e.append(error)
        N.append(c)

        tabla = []
        tabla.append([c, x, f, error])

    except Exception as e:
        print(f"1: {e}")

        tabla = [[0, 0, 0, 0]]

        df = pd.DataFrame(tabla, columns=["I", "Xi", "F(Xi)", "E"])

        x_vals = np.linspace(X0 - 5, X0 + 5, 400)
        y_vals = [eval(Fun, {"x": val, "math": math}) for val in x_vals]

        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label=f'f(x) = {Fun}', color='blue')
        plt.axhline(0, color='black', linewidth=1)
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

        resultado = "Error"

        return resultado, df.to_html(index=False, classes='table table-striped text-center'), img_uri


    while error > Tol and abs(f) > 1e-12 and c < Niter:
        
        try:

            x_new = eval(g, {"x": x, "math": math})  
            fe = eval(Fun, {"x": x_new, "math": math})  

            Error = abs(x_new - x)  
            error = Error / abs(x_new) if x_new != 0 else float('inf')  

            c += 1
            fn.append(fe)
            xn.append(x_new)
            N.append(c)
            E.append(Error)
            e.append(error)
            tabla.append([c, x_new, fe, error])

            x = x_new  
            f = fe 

        except Exception as e:
            print(f"2: {e}")

            df = pd.DataFrame(tabla, columns=["I", "Xi", "F(Xi)", "E"])

            x_vals = np.linspace(X0 - 5, X0 + 5, 400)
            y_vals = [eval(Fun, {"x": val, "math": math}) for val in x_vals]

            plt.figure(figsize=(8, 6))
            plt.plot(x_vals, y_vals, label=f'f(x) = {Fun}', color='blue')
            plt.axhline(0, color='black', linewidth=1)
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

            resultado = "Error"

            return resultado, df.to_html(index=False, classes='table table-striped text-center'), img_uri

    resultado = ""
    if abs(f) < 1e-12:
        resultado = f"{x} es raíz de f(x)"
    elif error < Tol:
        resultado = f"{x} es una aproximación de una raíz de f(x) con tolerancia {Tol}"
    else:
        df = pd.DataFrame(tabla, columns=["I", "Xi", "F(Xi)", "E"])

        x_vals = np.linspace(X0 - 5, X0 + 5, 400) 
        y_vals = [eval(Fun, {"x": val, "math": math}) for val in x_vals] 

        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, label=f'f(x) = {Fun}', color='blue')
        plt.axhline(0, color='black', linewidth=1)  
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

        resultado = f'Error en la iteracion {Niter}, ultima aproximacion: {x}'

        return resultado, df.to_html(index=False, classes='table table-striped text-center'), img_uri

    df = pd.DataFrame(tabla, columns=["I", "Xi", "F(Xi)", "E"])

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