from django.shortcuts import render
from .forms import PuntoFijoForm, NewtonForm, ReglaFalsaForm, SecanteForm

from .metodos import Puntofijo, Newton, Reglafalsa, Secante


def biseccion(request):
    return render(request, "biseccion.html")

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

def raices_multiples(request):
    return render(request, "raices_multiples.html")

def metodo_punto_fijo(request):
    if request.method == 'POST':
        form = PuntoFijoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            resultado, tabla, imagen = Puntofijo.punto_fijo(**data)
            return render(request, 'result_pf.html', {'resultado': resultado, 'tabla': tabla, 'imagen': imagen})
    else:
        form = PuntoFijoForm()
    return render(request, 'punto_fijo.html', {'form': form})
