import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

pd.options.display.float_format = "{:.8f}".format

def reglafalsaDC( a, b, Tol, Niter, Fun):

    nlist = []
    xrlist= []
    fxrlist=[]
    E=[]
    tabla = []
    a = a
    b = b
    Tol = Tol
    Niter = Niter
    Fun = Fun

    x = a
    fa = eval(Fun)
    x = b
    fb = eval(Fun)
    if fa == 0:
        s=a
        E=0
        print(a, 'es raiz de f(x)')
    elif fb == 0:
        s=b
        E=0
        print(b, 'es raiz de f(x)')
    if fa*fb < 0:
        i = 0
        nlist.append(i)
        xr = b - ((fb*(a-b))/(fa-fb))
        xrlist.append(xr)
        x = xr
        fxr = eval(Fun)
        fxrlist.append(fxr)
        Error = 100
        E.append(Error)
        tabla.append([i, x, fxr, Error])
        while E[i] > Tol and fxr != 0 and i < Niter:
            if fa*fxr < 0:
                b = xr
                x = b
                fb = eval(Fun)
            else:
                a = xr
                x = a
                fa = eval(Fun)
            xra = xr
            xr = b - ((fb*(a-b))/(fa-fb))
            xrlist.append(xr)
            x = xr
            fxr = eval(Fun)
            fxrlist.append(fxr)
            Error = abs(xr-xra)
            E.append(Error)
            i+=1
            nlist.append(i)
            tabla.append([i, x, fxr, Error])
            if fxr == 0:
                s=x
                df = pd.DataFrame({
                    "i": nlist,
                    "Xr": xrlist,
                    "Fxr": fxrlist,
                    "Error": E
                })
                print(df.to_string(index=False))
                break
            elif Error <= Tol:
                s=x
                df = pd.DataFrame({
                    "i": nlist,
                    "Xm": xrlist,
                    "Fm": fxrlist,
                    "Error": E
                })
                print(df.to_string(index=False), '\n')

                print(s,"es una aproximacion de un raiz de f(x) con una Tolerancia", Tol,'\n')
                break
        else:
            s=x
            print("Fracaso en ",Niter, " iteraciones ")
    else:
        print('El intervalo es inadecuado')

    
    df_resultado = pd.DataFrame(tabla, columns=["I", "Xi", "F(Xi)", "E"])
    tabla_html = df_resultado.to_html(index=False, classes='table table-striped text-center')

    x_vals = np.linspace(min(xrlist) - 1, max(xrlist) + 1, 100)
    y_vals = [eval(Fun, {"x": val, "math": math}) for val in x_vals]

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {Fun}', color='blue')
    plt.axhline(0, color='black', linewidth=1)
    plt.scatter(xrlist[-1], 0, color='red', zorder=5, label=f'Raíz: {round(xrlist[-1], 4)}')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Método de la Regla Falsa")
    plt.legend()
    plt.grid()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode()
    img_uri = f"data:image/png;base64,{string}"

    return s, tabla_html, img_uri

def reglafalsaCS( a, b, Tol, Niter, Fun):

    nlist = []
    xrlist= []
    fxrlist=[]
    E=[]
    tabla = []
    a = a
    b = b
    Tol = Tol
    Niter = Niter
    Fun = Fun

    x = a
    fa = eval(Fun)
    x = b
    fb = eval(Fun)
    if fa == 0:
        s=a
        E=0
        print(a, 'es raiz de f(x)')
    elif fb == 0:
        s=b
        E=0
        print(b, 'es raiz de f(x)')
    if fa*fb < 0:
        i = 0
        nlist.append(i)
        xr = b - ((fb*(a-b))/(fa-fb))
        xrlist.append(xr)
        x = xr
        fxr = eval(Fun)
        fxrlist.append(fxr)
        Error = 100
        E.append(Error)
        tabla.append([i, x, fxr, Error])
        while E[i] >= Tol and fxr != 0 and i < Niter:
            if fa*fxr < 0:
                b = xr
                x = b
                fb = eval(Fun)
            else:
                a = xr
                x = a
                fa = eval(Fun)
            xra = xr
            xr = b - ((fb*(a-b))/(fa-fb))
            xrlist.append(xr)
            x = xr
            fxr = eval(Fun)
            fxrlist.append(fxr)
            Error = abs((xr-xra)/xr)
            E.append(Error)
            i+=1
            nlist.append(i)
            tabla.append([i, x, fxr, Error])
            if fxr == 0:
                s=x
                df = pd.DataFrame({
                    "i": nlist,
                    "Xr": xrlist,
                    "Fxr": fxrlist,
                    "Error": E
                })
                print(df.to_string(index=False))
                break
            elif Error < Tol:
                s=x
                df = pd.DataFrame({
                    "i": nlist,
                    "Xm": xrlist,
                    "Fm": fxrlist,
                    "Error": E
                })
                print(df.to_string(index=False), '\n')

                print(s,"es una aproximacion de un raiz de f(x) con una Tolerancia", Tol,'\n')
                break
        else:
            s=x
            print("Fracaso en ",Niter, " iteraciones ")
    else:
        print('El intervalo es inadecuado')

    
    df_resultado = pd.DataFrame(tabla, columns=["I", "Xi", "F(Xi)", "E"])
    tabla_html = df_resultado.to_html(index=False, classes='table table-striped text-center')

    x_vals = np.linspace(min(xrlist) - 1, max(xrlist) + 1, 100)
    y_vals = [eval(Fun, {"x": val, "math": math}) for val in x_vals]

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {Fun}', color='blue')
    plt.axhline(0, color='black', linewidth=1)
    plt.scatter(xrlist[-1], 0, color='red', zorder=5, label=f'Raíz: {round(xrlist[-1], 4)}')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Método de la Regla Falsa")
    plt.legend()
    plt.grid()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode()
    img_uri = f"data:image/png;base64,{string}"

    return s, tabla_html, img_uri