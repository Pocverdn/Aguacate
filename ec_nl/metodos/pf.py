import pandas as pd
import math

def punto_fijo(X0, Tol, Niter, Fun, g):
    fn = []
    xn = []
    E = []
    N = []
    x = X0
    f = eval(Fun, {"x": x, "math": math})
    c = 0
    Error = 100
    fn.append(f)
    xn.append(x)
    E.append(Error)
    N.append(c)
    tabla = []
    tabla.append([c, x, f, Error])

    while Error > Tol and f != 0 and c < Niter:
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

    resultado = ""
    if f == 0:
        resultado = f"{x} es raíz de f(x)"
    elif Error < Tol:
        resultado = f"{x} es una aproximación de una raíz de f(x) con tolerancia {Tol}"
    else:
        resultado = f"Fracaso en {Niter} iteraciones"

    df = pd.DataFrame(tabla, columns=["I", "Xi", "F(Xi)", "E"])
    return resultado, df.to_html(classes='table table-striped')