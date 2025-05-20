from django.shortcuts import render

from .forms import JacobiForm, GausseidelForm, SORForm, TodosForm
from .metodos.jacobi import jacobi
from .metodos.gauss_seidel import gausseidel
from .metodos.parser import parse_matrix
from .metodos.SOR import SOR

import numpy as np

from io import BytesIO
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, Table, TableStyle
from reportlab.lib import colors
import base64
import pandas as pd


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
                modo = form.cleaned_data['Modo']

                tabla, solucion = gausseidel(x0, A, b, tol, niter, modo)
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


def todos_view(request):
    if request.method == 'POST':
        form = TodosForm(request.POST)
        if form.is_valid():

            resultados = {}

            A = parse_matrix(form.cleaned_data['A'])
            b = parse_matrix(form.cleaned_data['b'])
            x0 = parse_matrix(form.cleaned_data['x0'])
            tol = form.cleaned_data['tol']
            niter = form.cleaned_data['niter']
            modo = form.cleaned_data['Modo']

            tabla, solucion = jacobi(x0, A, b, tol, niter, modo)
            resultados['Jacobi'] = {'tabla': tabla, 'solucion': solucion}

            tabla, solucion = gausseidel(x0, A, b, tol, niter, modo)
            resultados['Gauss'] = {'tabla': tabla, 'solucion': solucion}

            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer, pagesize=letter)
            elements = []

            for metodo, datos in resultados.items():
                elements.append(Paragraph(f"<b>{metodo}</b>", style=None))
                elements.append(Paragraph(str(datos['solucion']), style=None))
                tabla = pd.read_html(datos['tabla'])[0]
                table_data = [list(tabla.columns)] + tabla.values.tolist()
                elements.append(Table(table_data, style=[('GRID', (0,0), (-1,-1), 1, colors.black)]))
                elements.append(Spacer(1, 12))

            doc.build(elements)
            buffer.seek(0)
            return FileResponse(buffer, as_attachment=True, filename="resultados.pdf")

    else:
        form = TodosForm()

    return render(request, 'todosN.html', {'form': form})
