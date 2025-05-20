from django.shortcuts import render

from .forms import JacobiForm, GausseidelForm, SORForm
from .metodos.jacobi import jacobi
from .metodos.gauss_seidel import gausseidel
from .metodos.parser import parse_matrix
from .metodos.SOR import SOR

import numpy as np

def jacobi_view(request):
    resultado = None
    errores = None

    if request.method == 'POST':
        form = JacobiForm(request.POST)
        if form.is_valid():
            try:
                A_text = form.cleaned_data['A']
                A = parse_matrix(A_text)
                b_text = form.cleaned_data['b']
                b = parse_matrix(b_text)
                x0_text = form.cleaned_data['x0']
                x0 = parse_matrix(x0_text)
                tol = form.cleaned_data['tol']
                niter = form.cleaned_data['niter']
                modo = form.cleaned_data['Modo']

                tabla, solucion = jacobi(x0, A, b, tol, niter, modo)
                resultado = {
                    'solucion': solucion,
                    'tabla': tabla,
                }
            except Exception as e:
                resultado = None
                tabla = [f"Error en los datos: {e}"]

            return render(request, 'result_jacobi.html', {'form': form, 'resultado': resultado, 'tabla': tabla})
    else:
        form = JacobiForm()

    return render(request, 'jacobi.html', {'form': form})

def gausseidel_view(request):
    resultado = None
    errores = None

    if request.method == 'POST':
        form = GausseidelForm(request.POST)
        if form.is_valid():
            try:
                A_text = form.cleaned_data['A']
                A = parse_matrix(A_text)
                b_text = form.cleaned_data['b']
                b = parse_matrix(b_text)
                x0_text = form.cleaned_data['x0']
                x0 = parse_matrix(x0_text)
                tol = form.cleaned_data['tol']
                niter = form.cleaned_data['niter']

                tabla, solucion = gausseidel(x0, A, b, tol, niter)
                resultado = {
                    'solucion': solucion,
                    'tabla': tabla,
                }
            except Exception as e:
                resultado = None
                tabla = [f"Error en los datos: {e}"]
            return render(request, 'result_gausseidel.html', {'form': form, 'resultado': resultado, 'tabla': tabla})
    else:
        form = GausseidelForm()

    return render(request, 'gausseidel.html', {'form': form})

def SOR_view(request):
    resultado = None
    errores = None

    if request.method == 'POST':
        form = SORForm(request.POST)
        if form.is_valid():
            try:
                A_text = form.cleaned_data['A']
                A = parse_matrix(A_text)
                b_text = form.cleaned_data['b']
                b = parse_matrix(b_text)
                x0_text = form.cleaned_data['x0']
                x0 = parse_matrix(x0_text)
                tol = form.cleaned_data['tol']
                niter = form.cleaned_data['niter']
                w = form.cleaned_data['w']
                modo = form.cleaned_data['Modo']

                tabla, solucion = SOR(x0, A, b, tol, niter, w, modo)
                resultado = {
                    'solucion': solucion,
                    'tabla': tabla,
                }
            except Exception as e:
                resultado = None
                tabla = [f"Error en los datos: {e}"]
            return render(request, 'result_SOR.html', {'form': form, 'resultado': resultado, 'tabla': tabla})
    else:
        form = SORForm()

    return render(request, 'SOR.html', {'form': form})