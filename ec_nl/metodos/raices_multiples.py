import pandas as pd
import math

def raices_multiples(X0, Tol, Niter, Fun, df, ddf):
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
    return resultado, df.to_html(index=False, classes='table table-striped text-center')
