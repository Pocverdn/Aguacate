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

from sympy import sympify, symbols


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
            nx_text = form.cleaned_data['nx']
            nx = parse_matrix(nx_text)
            ny_text = form.cleaned_data['ny']
            ny = parse_matrix(ny_text)
            grado = form.cleaned_data['grado']


            x_sym = symbols('x')

            pol, grafica = vandermonde(x,y,grado)
            if pol != "Error":
                expr = sympify(pol)

                eval_point = [expr.subs(x_sym, val).evalf() for val in nx]

                print(eval_point)

                e = abs(eval_point[0] - ny[0])
                resultados['vandermonde'] = {'pol': pol, 'grafica': grafica, 'eval': eval_point, 'error': e}
            else:
                resultados['vandermonde'] = {'pol': pol, 'grafica': grafica, 'eval': None, 'error': None}

            pol, grafica = lagrange(x,y)
            if pol != "Error":
                expr = sympify(pol)

                eval_point = [expr.subs(x_sym, val).evalf() for val in nx]
                e = abs(eval_point[0] - ny[0])
                resultados['lagrange'] = {'pol': pol, 'grafica': grafica, 'eval': eval_point, 'error': e}
            else:
                resultados['lagrange'] = {'pol': pol, 'grafica': grafica, 'eval': None, 'error': None}

            pol, grafica = newtonint(x,y)
            if pol != "Error":

                expr = sympify(pol)

                eval_point = [expr.subs(x_sym, val).evalf() for val in nx]
                e = abs(eval_point[0] - ny[0])
                resultados['newtonint'] = {'pol': pol, 'grafica': grafica, 'eval': eval_point, 'error': e}
            else:
                resultados['newtonint'] = {'pol': pol, 'grafica': grafica, 'eval': None, 'error': None}

            pol, grafica, polinomiosC = spline_cubico(x,y)
            if pol != "Error":
                results = []
                error = []
                for p in polinomiosC:
                    expr = sympify(p)
                    eval_point = [expr.subs(x_sym, val).evalf() for val in nx]
                    e = abs(eval_point[0] - ny[0])
                    results.append(eval_point)
                    error.append(e)

                ne = sum(error) / len(error)
                resultados['spline_cubico'] = {'pol': pol, 'grafica': grafica, 'eval': results, 'error': ne}
            else:
                resultados['spline_cubico'] = {'pol': pol, 'grafica': grafica, 'eval': None, 'error': None}

            pol, grafica, polinomios = spline_lineal(x,y)
            
            if pol != "Error":
                results = []
                error = []
                for p in polinomios:
                    expr = sympify(p)
                    eval_point = [expr.subs(x_sym, val).evalf() for val in nx]
                    e = abs(eval_point[0] - ny[0])
                    results.append(eval_point)
                    error.append(e)
                    
                ne = sum(error) / len(error)
                resultados['spline_lineal'] = {'pol': pol, 'grafica': grafica, 'eval': results, 'error': ne}
            else:
                resultados['spline_lineal'] = {'pol': pol, 'grafica': grafica, 'eval': None, 'error': None}
                

            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer, pagesize=letter)
            elements = []

            for metodo, datos in resultados.items():
                elements.append(Paragraph(f"<b>{metodo}</b>", style=None))
                elements.append(Paragraph(str(datos['pol']), style=None))
                elements.append(Paragraph(str(datos['eval']), style=None))
                elements.append(Paragraph(str(datos['error']), style=None))
                if datos['grafica']:
                    image_data = base64.b64decode(datos['grafica'].split(',')[1])
                    img = Image(BytesIO(image_data), width=400, height=300)
                    elements.append(img)
                elements.append(Spacer(1, 12))

            
            resumen_data = [
                ['Método', 'Polinomio', 'Evaluación', 'Error'],
                ['Vandermonde', 
                Paragraph(str(resultados['vandermonde']['pol'])), 
                Paragraph(str(resultados['vandermonde']['eval'])), 
                Paragraph(str(resultados['vandermonde']['error']))],
                ['Lagrange', 
                Paragraph(str(resultados['lagrange']['pol'])), 
                Paragraph(str(resultados['lagrange']['eval'])), 
                Paragraph(str(resultados['lagrange']['error']))],
                ['Newton', 
                Paragraph(str(resultados['newtonint']['pol'])), 
                Paragraph(str(resultados['newtonint']['eval'])), 
                Paragraph(str(resultados['newtonint']['error']))],
                ['Spline Cúbico', 
                Paragraph("Varios polinomios" if resultados['spline_cubico']['pol'] != "Error" else "Error"), 
                Paragraph(str(resultados['spline_cubico']['eval'])), 
                Paragraph(str(resultados['spline_cubico']['error']))],
                ['Spline Lineal', 
                Paragraph("Varios polinomios" if resultados['spline_lineal']['pol'] != "Error" else "Error"), 
                Paragraph(str(resultados['spline_lineal']['eval'])), 
                Paragraph(str(resultados['spline_lineal']['error']))]
            ]


            mejor_metodo = min(resultados, key=lambda k: resultados[k]['error'])

            elements.append(Spacer(1, 24))
            if mejor_metodo:
                mensaje_final = f"El mejor método según el menor número de iteraciones es: <b>{mejor_metodo}</b> con un error de {resultados[mejor_metodo]['error']}."
            else:
                mensaje_final = "No se pudo determinar un mejor método por errores en los datos."

            elements.append(Spacer(1, 24))
            elements.append(Paragraph("<b>Resumen de los metodos</b>", style=None))
            elements.append(Table(resumen_data, style=[('GRID', (0,0), (-1,-1), 1, colors.black)]))

            elements.append(Paragraph(mensaje_final, style=None))
        

            doc.build(elements)
            buffer.seek(0)
            return FileResponse(buffer, as_attachment=True, filename="resultados.pdf")

    else:
        form = TodoForm()

    return render(request, 'todosInt.html', {'form': form})