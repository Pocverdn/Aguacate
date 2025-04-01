from django.shortcuts import render
from .forms import PuntoFijoForm, NewtonForm, BiseccionForm, RaicesMultiplesForm

from .metodos import Puntofijo, Newton, Reglafalsa, Secante
 
from .metodos.biseccion import biseccion
from .metodos.raices_multiples import raices_multiples
from sympy import symbols, sympify, lambdify


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

            resultado, tabla = biseccion(**data)
            print(resultado, tabla)
            return render(request, 'result_biseccion.html', {
                'resultado': resultado,
                'tabla': tabla
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
            else:
                resultado, tabla, imagen = Reglafalsa.reglafalsaDC(**data)
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
            else:
                resultado, tabla, imagen = Newton.metodo_newton(**data)
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
            else:
                resultado, tabla, imagen = Secante.secanteDC(**data)
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

            resultado, tabla = raices_multiples(**data)
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
            else:
                resultado, tabla, imagen = Puntofijo.punto_fijo(**data)
            return render(request, 'result_pf.html', {'resultado': resultado, 'tabla': tabla, 'imagen': imagen})
    else:
        form = PuntoFijoForm()
    return render(request, 'punto_fijo.html', {'form': form})
