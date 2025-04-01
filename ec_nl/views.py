from django.shortcuts import render
from .forms import PuntoFijoForm, NewtonForm, BiseccionForm, RaicesMultiplesForm

from .metodos import pf, Newton
 
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
    return render(request, "regla_falsa.html")

def newton(request):
    if request.method == 'POST':
        form = NewtonForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            resultado, tabla = Newton.metodo_newton(**data)
            return render(request, 'result_ne.html', {'resultado': resultado, 'tabla': tabla})
    else:
        form = PuntoFijoForm()
    return render(request, 'newton.html', {'form': form})



def secante(request):
    return render(request, "secante.html")


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
            resultado, tabla = pf.punto_fijo(**data)
            return render(request, 'result_pf.html', {'resultado': resultado, 'tabla': tabla})
    else:
        form = PuntoFijoForm()
    return render(request, 'punto_fijo.html', {'form': form})
