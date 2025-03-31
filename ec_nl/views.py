from django.shortcuts import render
from .forms import PuntoFijoForm, NewtonForm

from .metodos import pf, Newton


def biseccion(request):
    return render(request, "biseccion.html")

def regla_falsa(request):
    return render(request, "regla_falsa.html")

def newton(request):
    if request.method == 'POST':
        form = NewtonForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            resultado, tabla, imagen = Newton.metodo_newton(**data)
            return render(request, 'result_ne.html', {'resultado': resultado, 'tabla': tabla, 'imagen': imagen})
    else:
        form = NewtonForm()
    return render(request, 'newton.html', {'form': form})



def secante(request):
    return render(request, "secante.html")

def raices_multiples(request):
    return render(request, "raices_multiples.html")

def metodo_punto_fijo(request):
    if request.method == 'POST':
        form = PuntoFijoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            resultado, tabla, imagen = pf.punto_fijo(**data)
            return render(request, 'result_pf.html', {'resultado': resultado, 'tabla': tabla, 'imagen': imagen})
    else:
        form = PuntoFijoForm()
    return render(request, 'punto_fijo.html', {'form': form})
