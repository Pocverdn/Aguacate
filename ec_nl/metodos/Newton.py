import pandas as pd
import math

def metodo_newton(X0, Tol, Niter, Fun, df_expr):
    fn = []
    xn = []
    E = []
    N = []
    x = X0
    f = eval(Fun, {"x": x, "math": math})
    derivada = eval(df_expr, {"x": x, "math": math})
    c = 0
    Error = 100               
    fn.append(f)
    xn.append(x)
    E.append(Error)
    N.append(c)

    tabla = []
    tabla.append([c, x, f, Error])

    while Error > Tol and f != 0 and derivada != 0 and c < Niter:
        x = x - f / derivada
        derivada = eval(df_expr, {"x": x, "math": math})
        f = eval(Fun, {"x": x, "math": math})
        fn.append(f)
        xn.append(x)
        c += 1
        Error = abs(xn[c] - xn[c - 1])
        N.append(c)
        E.append(Error)
        tabla.append([c, x, f, Error])

    if f == 0:
        resultado = f"{x} es raíz de f(x)"
    elif Error < Tol:
        resultado = f"{x} es una aproximación de una raíz de f(x) con tolerancia {Tol}"
    else:
        resultado = f"Fracaso en {Niter} iteraciones"

    df_resultado = pd.DataFrame(tabla, columns=["I", "Xi", "F(Xi)", "E"])
    tabla_html = df_resultado.to_html(index=False, classes='table table-striped text-center')

    return resultado, tabla_html
