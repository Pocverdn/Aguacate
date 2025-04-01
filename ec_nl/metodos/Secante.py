import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

pd.options.display.float_format = "{:.16f}".format

def secanteDC( X0, X1, Tol, Niter, Fun):

    nlist = []
    xnlist= []
    fxnlist=[]
    E=[]
    tabla = []
    x = X0
    f0 = eval(Fun)
    x = X1
    f1= eval(Fun)
    if f0 == 0:
        s=X0
        E=0
        print(s, 'es raiz de f(x)')
    elif f1 == 0:
        s=X1
        E=0
        print(s, 'es raiz de f(x)')
    i = 0
    xnlist.append(X1)
    fxnlist.append(f1)
    nlist.append(i)
    Error = 100
    E.append(Error)
    tabla.append([i, X1, f1, Error])
    while E[i] > Tol and f1 != 0 and i < Niter:
        x=X1-((f1*(X1-X0))/(f1-f0))
        f=eval(Fun)
        X0 = X1
        X1 = x
        f0 = f1
        f1 = f
        xnlist.append(X1)
        fxnlist.append(f1)
        i += 1
        Error=abs(X1-X0)
        nlist.append(i)
        E.append(Error)
        tabla.append([i, X1, f1, Error])
        if f == 0:
            s=x
            df = pd.DataFrame({
                "i": nlist,
                "Xn": xnlist,
                "Fxn": fxnlist,
                "Error": E
            })
            print(df.to_string(index=False))

            print(s,"Es una raiz de f(x)")
            break
        elif Error <= Tol:
            s=x
            df = pd.DataFrame({
                "i": nlist,
                "Xn": xnlist,
                "Fxn": fxnlist,
                "Error": E
            })
            print(df.to_string(index=False), '\n')

            print(s,"es una aproximacion de un raiz de f(x) con una Tolerancia", Tol,'\n')
            break
    else:
        s=x
        print("Fracaso en ", Niter, " iteraciones ")
    
    df_resultado = pd.DataFrame(tabla, columns=["I", "Xi", "F(Xi)", "E"])
    tabla_html = df_resultado.to_html(index=False, classes='table table-striped text-center')

    x_vals = np.linspace(min(xnlist) - 1, max(xnlist) + 1, 100)
    y_vals = [eval(Fun, {"x": val, "math": math}) for val in x_vals]

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {Fun}', color='blue')
    plt.axhline(0, color='black', linewidth=1)
    plt.scatter(xnlist[-1], 0, color='red', zorder=5, label=f'Raíz: {round(xnlist[-1], 4)}')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Método de la Secante")
    plt.legend()
    plt.grid()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode()
    img_uri = f"data:image/png;base64,{string}"

    return s, tabla_html, img_uri

def secanteCS( X0, X1, Tol, Niter, Fun):

    nlist = []
    xnlist= []
    fxnlist=[]
    E=[]
    tabla = []
    x = X0
    f0 = eval(Fun)
    x = X1
    f1= eval(Fun)
    if f0 == 0:
        s=X0
        E=0
        print(s, 'es raiz de f(x)')
    elif f1 == 0:
        s=X1
        E=0
        print(s, 'es raiz de f(x)')
    i = 0
    xnlist.append(X1)
    fxnlist.append(f1)
    nlist.append(i)
    Error = 100
    E.append(Error)
    tabla.append([i, X1, f1, Error])
    while E[i] >= Tol and f1 != 0 and i < Niter:
        x=X1-((f1*(X1-X0))/(f1-f0))
        f=eval(Fun)
        X0 = X1
        X1 = x
        f0 = f1
        f1 = f
        xnlist.append(X1)
        fxnlist.append(f1)
        i += 1
        Error=abs((xnlist[i]-xnlist[i-1])/xnlist[i])
        nlist.append(i)
        E.append(Error)
        tabla.append([i, X1, f1, Error])
        if f == 0:
            s=x
            df = pd.DataFrame({
                "i": nlist,
                "Xn": xnlist,
                "Fxn": fxnlist,
                "Error": E
            })
            print(df.to_string(index=False))

            print(s,"Es una raiz de f(x)")
            break
        elif Error < Tol:
            s=x
            df = pd.DataFrame({
                "i": nlist,
                "Xn": xnlist,
                "Fxn": fxnlist,
                "Error": E
            })
            print(df.to_string(index=False), '\n')

            print(s,"es una aproximacion de un raiz de f(x) con una Tolerancia", Tol,'\n')
            break
    else:
        s=x
        print("Fracaso en ", Niter, " iteraciones ")
    
    df_resultado = pd.DataFrame(tabla, columns=["I", "Xi", "F(Xi)", "E"])
    tabla_html = df_resultado.to_html(index=False, classes='table table-striped text-center')

    x_vals = np.linspace(min(xnlist) - 1, max(xnlist) + 1, 100)
    y_vals = [eval(Fun, {"x": val, "math": math}) for val in x_vals]

    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {Fun}', color='blue')
    plt.axhline(0, color='black', linewidth=1)
    plt.scatter(xnlist[-1], 0, color='red', zorder=5, label=f'Raíz: {round(xnlist[-1], 4)}')
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Método de la Secante")
    plt.legend()
    plt.grid()

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read()).decode()
    img_uri = f"data:image/png;base64,{string}"

    return s, tabla_html, img_uri