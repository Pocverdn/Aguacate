from django.shortcuts import render
from .forms import PuntoFijoForm, NewtonForm, BiseccionForm, RaicesMultiplesForm, ReglaFalsaForm, SecanteForm, todosForm

from .metodos import Puntofijo, Newton, Reglafalsa, Secante
 
from .metodos.Biseccion import biseccion
from .metodos.Raices_multiples import raices_multiples
from sympy import symbols, sympify, lambdify

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas



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
                'tabla': tabla
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
            resultados = []

            if modo == 'cs':
                resultados.append(Puntofijo.punto_fijoCS(**data))
                resultados.append(Secante.secanteCS(**data))
                resultados.append(Reglafalsa.reglafalsaCS(**data))
                resultados.append(Newton.metodo_newtonCS(**data))
                resultados.append(biseccion(**data))
                resultados.append(raices_multiples(**data))
            else:
                resultados.append(Puntofijo.punto_fijo(**data))
                resultados.append(Secante.secanteDC(**data))
                resultados.append(Reglafalsa.reglafalsaDC(**data))
                resultados.append(Newton.metodo_newton(**data))
                resultados.append(biseccion(**data))
                resultados.append(raices_multiples(**data))

            buffer = io.BytesIO()
            p = canvas.Canvas(buffer)
            p.setFont("Helvetica", 12)
            p.drawString(100, 800, "Resultados de Métodos Numéricos")

            y = 770
            for i, (resultado, tabla, imagen) in enumerate(resultados):
                p.drawString(100, y, f"Método {i+1} - Resultado: {resultado}")
                y -= 20
                for fila in tabla:
                    p.drawString(100, y, str(fila))
                    y -= 15
                y -= 20

            p.showPage()
            p.save()
            buffer.seek(0)

            return FileResponse(buffer, as_attachment=True, filename='resultados_metodos.pdf')
    else:
        form = todosForm()
    return render(request, 'todos.html', {'form': form})