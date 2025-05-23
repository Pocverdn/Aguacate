from django.shortcuts import render
from .forms import VanderForm, LagrangeForm, NewtonintForm, SplineLinIntForm, SplineCubIntForm, TodoForm
from .metodos.vander import vandermonde
from .metodos.lagrange import lagrange
from .metodos.newtonint import newtonint
from .metodos.splinelin import spline_lineal
from .metodos.splinecub import spline_cubico
from .metodos.parser import parse_matrix

import matplotlib
matplotlib.use('Agg')
import numpy as np
from io import BytesIO
from django.http import FileResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, Table, TableStyle
from reportlab.lib import colors
import base64
import pandas as pd


def vander_view(request):

    if request.method == 'POST':
        form = VanderForm(request.POST)
        if form.is_valid():

            x_text = form.cleaned_data['x']
            x = parse_matrix(x_text)
            y_text = form.cleaned_data['y']
            y = parse_matrix(y_text)
            grado = form.cleaned_data['grado']
            pol, grafica = vandermonde(x,y,grado)

            if pol == "Error":
                return render(request, 'errorInt.html', {'pol': pol, 'grafica': grafica})

            resultado = {
                'solucion': pol,
                'grafica': grafica,
            }            

            return render(request, 'result_vander.html', {'form': form, 'resultado': resultado, 'grafica': grafica})
    else:
        form = VanderForm()

    return render(request, 'vander.html', {'form': form})

def lagrange_view(request):

    if request.method == 'POST':
        form = LagrangeForm(request.POST)
        if form.is_valid():

            x_text = form.cleaned_data['x']
            x = parse_matrix(x_text)
            y_text = form.cleaned_data['y']
            y = parse_matrix(y_text)
            pol, grafica = lagrange(x,y)

            if pol == "Error":
                return render(request, 'errorInt.html', {'pol': pol, 'grafica': grafica})

            resultado = {
                'solucion': pol,
                'grafica': grafica,
            }            

            return render(request, 'result_lagrange.html', {'form': form, 'resultado': resultado, 'grafica': grafica})
    else:
        form = LagrangeForm()

    return render(request, 'lagrange.html', {'form': form})

def newtonint_view(request):

    if request.method == 'POST':
        form = NewtonintForm(request.POST)
        if form.is_valid():

            x_text = form.cleaned_data['x']
            x = parse_matrix(x_text)
            y_text = form.cleaned_data['y']
            y = parse_matrix(y_text)
            pol, grafica = newtonint(x,y)

            if pol == "Error":
                return render(request, 'errorInt.html', {'pol': pol, 'grafica': grafica})

            resultado = {
                'solucion': pol,
                'grafica': grafica,
            }            

            return render(request, 'result_newtonint.html', {'form': form, 'resultado': resultado, 'grafica': grafica})
    else:
        form = NewtonintForm()

    return render(request, 'newtonint.html', {'form': form})

def spline_lin_view(request):

    if request.method == 'POST':
        form = SplineLinIntForm(request.POST)
        if form.is_valid():

            x_text = form.cleaned_data['x']
            x = parse_matrix(x_text)
            y_text = form.cleaned_data['y']
            y = parse_matrix(y_text)
            pol, grafica = spline_lineal(x,y)

            if pol == "Error":
                return render(request, 'errorInt.html', {'pol': pol, 'grafica': grafica})

            resultado = {
                'solucion': pol,
                'grafica': grafica,
            }            

            return render(request, 'result_spline_lin.html', {'form': form, 'resultado': resultado, 'grafica': grafica})
    else:
        form =SplineLinIntForm()

    return render(request, 'spline_lin.html', {'form': form})

def spline_cub_view(request):

    if request.method == 'POST':
        form = SplineCubIntForm(request.POST)
        if form.is_valid():

            x_text = form.cleaned_data['x']
            x = parse_matrix(x_text)
            y_text = form.cleaned_data['y']
            y = parse_matrix(y_text)
            pol, grafica = spline_cubico(x,y)

            if pol == "Error":
                return render(request, 'errorInt.html', {'pol': pol, 'grafica': grafica})

            resultado = {
                'solucion': pol,
                'grafica': grafica,
            }            

            return render(request, 'result_spline_cub.html', {'form': form, 'resultado': resultado, 'grafica': grafica})
    else:
        form =SplineLinIntForm()

    return render(request, 'spline_cub.html', {'form': form})


def todo_view(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():

            resultados = {}


            x_text = form.cleaned_data['x']
            x = parse_matrix(x_text)
            y_text = form.cleaned_data['y']
            y = parse_matrix(y_text)
            grado = form.cleaned_data['grado']

            pol, grafica = vandermonde(x,y,grado)
            resultados['Jacobi'] = {'pol': pol, 'grafica': grafica}

            pol, grafica = lagrange(x,y)
            resultados['lagrange'] = {'pol': pol, 'grafica': grafica}

            pol, grafica = newtonint(x,y)
            resultados['newton'] = {'pol': pol, 'grafica': grafica}

            pol, grafica = spline_cubico(x,y)
            resultados['spline_cubico'] = {'pol': pol, 'grafica': grafica}

            pol, grafica = spline_lineal(x,y)
            resultados['spline_lineal'] = {'pol': pol, 'grafica': grafica}
          

            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer, pagesize=letter)
            elements = []

            for metodo, datos in resultados.items():
                elements.append(Paragraph(f"<b>{metodo}</b>", style=None))
                elements.append(Paragraph(str(datos['pol']), style=None))
                if datos['grafica']:
                    image_data = base64.b64decode(datos['grafica'].split(',')[1])
                    img = Image(BytesIO(image_data), width=400, height=300)
                    elements.append(img)
                elements.append(Spacer(1, 12))
            

            doc.build(elements)
            buffer.seek(0)
            return FileResponse(buffer, as_attachment=True, filename="resultados.pdf")

    else:
        form = TodoForm()

    return render(request, 'todosInt.html', {'form': form})