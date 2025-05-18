from django.shortcuts import render
from .forms import PuntoFijoForm, NewtonForm, BiseccionForm, RaicesMultiplesForm, ReglaFalsaForm, SecanteForm, todosForm

from .metodos import Puntofijo, Newton, Reglafalsa, Secante
 
from .metodos.Biseccion import biseccion
from .metodos.Raices_multiples import raices_multiples
from sympy import symbols, sympify, lambdify

from io import BytesIO
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, Table, TableStyle
from reportlab.lib import colors
import base64
import pandas as pd



def biseccion_view(request):
    if request.method == 'POST':
        print("entre")
        form = BiseccionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            x = symbols('x')
            expr = sympify(data.get("fun"))
            f = lambdify(x, expr)
            data["fun"] = f

            resultado, tabla, img = biseccion(**data)

            if resultado == "Error":
                return render(request, 'error.html', {'resultado': resultado, 'tabla': tabla, 'imagen': img})
            print(resultado, tabla)
            return render(request, 'result_biseccion.html', {
                'resultado': resultado,
                'tabla': tabla,
                "imagen":img
            })
    else:
        form = BiseccionForm()

    return render(request, 'biseccion.html', {'form': form})

def regla_falsa(request):
    if request.method == 'POST':
        form = ReglaFalsaForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            modo = data.pop('Modo', None)
            if modo == 'cs':
                resultado, tabla, imagen = Reglafalsa.reglafalsaCS(**data)
                if resultado == "Error":
                    return render(request, 'error.html', {'resultado': resultado, 'tabla': tabla, 'imagen': imagen})
            else:
                resultado, tabla, imagen = Reglafalsa.reglafalsaDC(**data)
                if resultado == "Error":
                    return render(request, 'error.html', {'resultado': resultado, 'tabla': tabla, 'imagen': imagen})
            return render(request, 'result_rf.html', {'resultado': resultado, 'tabla': tabla, 'imagen': imagen})
    else:
        form = ReglaFalsaForm()
    return render(request, 'regla_falsa.html', {'form': form})

def newton(request):
    if request.method == 'POST':
        form = NewtonForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            modo = data.pop('Modo', None)
            if modo == 'cs':
                resultado, tabla, imagen = Newton.metodo_newtonCS(**data)
                if resultado == "Error":
                    return render(request, 'error.html', {'resultado': resultado, 'tabla': tabla, 'imagen': imagen})
            else:
                resultado, tabla, imagen = Newton.metodo_newton(**data)
                if resultado == "Error":
                    return render(request, 'error.html', {'resultado': resultado, 'tabla': tabla, 'imagen': imagen})
            return render(request, 'result_ne.html', {'resultado': resultado, 'tabla': tabla, 'imagen': imagen})
    else:
        form = NewtonForm()
    return render(request, 'newton.html', {'form': form})

def secante(request):
    if request.method == 'POST':
        form = SecanteForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            modo = data.pop('Modo', None)
            if modo == 'cs':
                resultado, tabla, imagen = Secante.secanteCS(**data)
                if resultado == "Error":
                    return render(request, 'error.html', {'resultado': resultado, 'tabla': tabla, 'imagen': imagen})
            else:
                resultado, tabla, imagen = Secante.secanteDC(**data)
                if resultado == "Error":
                    return render(request, 'error.html', {'resultado': resultado, 'tabla': tabla, 'imagen': imagen})
            return render(request, 'result_sc.html', {'resultado': resultado, 'tabla': tabla, 'imagen': imagen})
    else:
        form = SecanteForm()
    return render(request, 'secante.html', {'form': form})

def raices_multiples_view(request):
    if request.method == 'POST':
        form = RaicesMultiplesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            x = symbols('x')
            print(data.get("Fun"))
            expr = sympify(data.get("Fun"))
            f = lambdify(x, expr)
            data["Fun"] = f

            expr = sympify(data.get("df"))
            df = lambdify(x, expr)
            data["df"] = df

            expr = sympify(data.get("ddf"))
            ddf = lambdify(x, expr)
            data["ddf"] = ddf

            resultado, tabla, img = raices_multiples(**data)
            return render(request, 'result_raices_multiples.html', {
                'resultado': resultado,
                'tabla': tabla,
                'imagen': img
            })
    else:
        form = RaicesMultiplesForm()

    return render(request, 'raices_multiples.html', {'form': form})

def metodo_punto_fijo(request):
    if request.method == 'POST':
        form = PuntoFijoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            modo = data.pop('Modo', None)
            if modo == 'cs':
                resultado, tabla, imagen = Puntofijo.punto_fijoCS(**data)
                if resultado == "Error":
                    return render(request, 'error.html', {'resultado': resultado, 'tabla': tabla, 'imagen': imagen})
            else:
                resultado, tabla, imagen = Puntofijo.punto_fijo(**data)
                if resultado == "Error":
                    return render(request, 'error.html', {'resultado': resultado, 'tabla': tabla, 'imagen': imagen})
            return render(request, 'result_pf.html', {'resultado': resultado, 'tabla': tabla, 'imagen': imagen})
    else:
        form = PuntoFijoForm()
    return render(request, 'punto_fijo.html', {'form': form})

def todos_view(request):
    if request.method == 'POST':
        form = todosForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            modo = data.pop('Modo', None)
            resultados = {}

            a = data.get("a")
            b = data.get("b")
            tol = data.get("tol")
            niter = data.get("niter")
            fun = data.get("fun")
            df = data.get("df")
            g = data.get("g")

            x = symbols('x')
            expr = sympify(data.get("fun"))
            fun2 = lambdify(x, expr)

            expr = sympify(data.get("df"))
            df2 = lambdify(x, expr)

            expr = sympify(data.get("ddf"))
            ddf2 = lambdify(x, expr)


            if modo == 'cs':
                resultados['Punto Fijo'] = {'mensaje': '', 'tabla': '', 'imagen': ''}
                resultados['Secante'] = {'mensaje': '', 'tabla': '', 'imagen': ''}
                resultados['Regla Falsa'] = {'mensaje': '', 'tabla': '', 'imagen': ''}
                resultados['Newton'] = {'mensaje': '', 'tabla': '', 'imagen': ''}
                resultados['Biseccion'] = {'mensaje': '', 'tabla': '', 'imagen': ''}
                resultados['Raices Multiples'] = {'mensaje': '', 'tabla': '', 'imagen': ''}

                resultados['Punto Fijo']['mensaje'], resultados['Punto Fijo']['tabla'], resultados['Punto Fijo']['imagen'] = Puntofijo.punto_fijoCS(a, tol, niter, fun, g)
                resultados['Secante']['mensaje'], resultados['Secante']['tabla'], resultados['Secante']['imagen'] = Secante.secanteCS(a, b, tol, niter, fun)
                resultados['Regla Falsa']['mensaje'], resultados['Regla Falsa']['tabla'], resultados['Regla Falsa']['imagen'] = Reglafalsa.reglafalsaCS(a, b, tol, niter, fun)
                resultados['Newton']['mensaje'], resultados['Newton']['tabla'], resultados['Newton']['imagen'] = Newton.metodo_newtonCS(a, tol, niter, fun, df)
                resultados['Biseccion']['mensaje'], resultados['Biseccion']['tabla'], resultados['Biseccion']['imagen'] = biseccion(a, b, tol, niter, fun2, modo)
                resultados['Raices Multiples']['mensaje'], resultados['Raices Multiples']['tabla'], resultados['Raices Multiples']['imagen'] = raices_multiples(a, tol, niter, fun2, df2, ddf2, modo)
            else:
                resultados['Punto Fijo'] = {'mensaje': '', 'tabla': '', 'imagen': ''}
                resultados['Secante'] = {'mensaje': '', 'tabla': '', 'imagen': ''}
                resultados['Regla Falsa'] = {'mensaje': '', 'tabla': '', 'imagen': ''}
                resultados['Newton'] = {'mensaje': '', 'tabla': '', 'imagen': ''}
                resultados['Biseccion'] = {'mensaje': '', 'tabla': '', 'imagen': ''}
                resultados['Raices Multiples'] = {'mensaje': '', 'tabla': '', 'imagen': ''}

                resultados['Punto Fijo']['mensaje'], resultados['Punto Fijo']['tabla'], resultados['Punto Fijo']['imagen'] = Puntofijo.punto_fijo(a, tol, niter, fun, g)
                resultados['Secante']['mensaje'], resultados['Secante']['tabla'], resultados['Secante']['imagen'] = Secante.secanteDC(a, b, tol, niter, fun)
                resultados['Regla Falsa']['mensaje'], resultados['Regla Falsa']['tabla'], resultados['Regla Falsa']['imagen'] = Reglafalsa.reglafalsaDC(a, b, tol, niter, fun)
                resultados['Newton']['mensaje'], resultados['Newton']['tabla'], resultados['Newton']['imagen'] = Newton.metodo_newton(a, tol, niter, fun, df)
                resultados['Biseccion']['mensaje'], resultados['Biseccion']['tabla'], resultados['Biseccion']['imagen'] = biseccion(a, b, tol, niter, fun2, modo)
                resultados['Raices Multiples']['mensaje'], resultados['Raices Multiples']['tabla'], resultados['Raices Multiples']['imagen'] = raices_multiples(a, tol, niter, fun2, df2, ddf2, modo)



            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer, pagesize=letter)
            elements = []

            for metodo, datos in resultados.items():
                elements.append(Paragraph(f"<b>{metodo}</b>", style=None))
                elements.append(Paragraph(str(datos['mensaje']), style=None))
                tabla = pd.read_html(datos['tabla'])[0]
                table_data = [list(tabla.columns)] + tabla.values.tolist()
                elements.append(Table(table_data, style=[('GRID', (0,0), (-1,-1), 1, colors.black)]))
                if datos['imagen']:
                    image_data = base64.b64decode(datos['imagen'].split(',')[1])
                    img = Image(BytesIO(image_data), width=400, height=300)
                    elements.append(img)
                elements.append(Spacer(1, 12))

            doc.build(elements)
            buffer.seek(0)
            return FileResponse(buffer, as_attachment=True, filename="resultados.pdf")

    else:
        form = todosForm()
    return render(request, 'todos.html', {'form': form})