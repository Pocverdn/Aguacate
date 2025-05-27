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
            A_text = form.cleaned_data['A']
            A = parse_matrix(A_text)
            b_text = form.cleaned_data['b']
            b = parse_matrix(b_text)
            x0_text = form.cleaned_data['x0']
            x0 = parse_matrix(x0_text)
            tol = form.cleaned_data['tol']
            niter = form.cleaned_data['niter']
            modo = form.cleaned_data['Modo']

            tabla, solucion, error, sp_radius = jacobi(x0, A, b, tol, niter, modo)

            if sp_radius < 1:
                convergencia = 'Radio espectral < 1, por lo tanto el método converge'
            else:
                convergencia = 'Radio espectral > 1, el método no converge'

            resultado = {
                'solucion': solucion,
                'radio': sp_radius,
                'convergencia': convergencia,
                'tabla': tabla,
            }

            if error == True:
                return render(request, 'errorN.html', {'form': form, 'resultado': resultado, 'tabla': tabla})

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
            A_text = form.cleaned_data['A']
            A = parse_matrix(A_text)
            b_text = form.cleaned_data['b']
            b = parse_matrix(b_text)
            x0_text = form.cleaned_data['x0']
            x0 = parse_matrix(x0_text)
            tol = form.cleaned_data['tol']
            niter = form.cleaned_data['niter']
            modo = form.cleaned_data['Modo']

            tabla, solucion, error, sp_radius = gausseidel(x0, A, b, tol, niter, modo)

            if sp_radius < 1:
                convergencia = 'Radio espectral < 1, por lo tanto el método converge'
            else:
                convergencia = 'Radio espectral > 1, el método no converge'

            resultado = {
                'solucion': solucion,
                'radio': sp_radius,
                'convergencia': convergencia,
                'tabla': tabla,
            }

            if error == True:
                return render(request, 'errorN.html', {'form': form, 'resultado': resultado, 'tabla': tabla})

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

            tabla, solucion, error, sp_radius = SOR(x0, A, b, tol, niter,w, modo)

            if sp_radius < 1:
                convergencia = 'Radio espectral < 1, por lo tanto el método converge'
            else:
                convergencia = 'Radio espectral > 1, el método no converge'

            resultado = {
                'solucion': solucion,
                'radio': sp_radius,
                'convergencia': convergencia,
                'tabla': tabla,
            }

            if error == True:
                return render(request, 'errorN.html', {'form': form, 'resultado': resultado, 'tabla': tabla})

            return render(request, 'result_SOR.html', {'form': form, 'resultado': resultado, 'tabla': tabla})
    else:
        form = SORForm()

    return render(request, 'SOR.html', {'form': form})


def todos_view(request):
    if request.method == 'POST':
        form = TodosForm(request.POST)
        if form.is_valid():

            try:

                resultados = {}

                A = parse_matrix(form.cleaned_data['A'])
                b = parse_matrix(form.cleaned_data['b'])
                x0 = parse_matrix(form.cleaned_data['x0'])
                tol = form.cleaned_data['tol']
                w1 = form.cleaned_data['w1']
                w2 = form.cleaned_data['w2']
                w3 = form.cleaned_data['w3']
                niter = form.cleaned_data['niter']
                modo = form.cleaned_data['Modo']

                tabla, solucion, error, sp_radius = jacobi(x0, A, b, tol, niter, modo)
                resultados['Jacobi'] = {'tabla': tabla, 'solucion': solucion, 'radio': sp_radius}

                tabla, solucion, error, sp_radius = gausseidel(x0, A, b, tol, niter, modo)
                resultados['Gauss'] = {'tabla': tabla, 'solucion': solucion, 'radio': sp_radius}

                tabla, solucion, error, sp_radius = SOR(x0, A, b, tol, niter, w1, modo)
                resultados['SOR1'] = {'tabla': tabla, 'solucion': solucion, 'radio': sp_radius}

                tabla, solucion, error, sp_radius = SOR(x0, A, b, tol, niter, w2, modo)
                resultados['SOR2'] = {'tabla': tabla, 'solucion': solucion, 'radio': sp_radius}
                
                tabla, solucion, error, sp_radius = SOR(x0, A, b, tol, niter, w3, modo)
                resultados['SOR3'] = {'tabla': tabla, 'solucion': solucion, 'radio': sp_radius}

                buffer = BytesIO()
                doc = SimpleDocTemplate(buffer, pagesize=letter)
                elements = []

                for metodo, datos in resultados.items():
                    elements.append(Paragraph(f"<b>{metodo}</b>", style=None))
                    elements.append(Paragraph(str(datos['solucion']), style=None))
                    elements.append(Paragraph(f"Radio espectral: {datos['radio']:.4f}", style=None))
                    tabla = pd.read_html(datos['tabla'])[0]
                    table_data = [list(tabla.columns)] + tabla.values.tolist()
                    elements.append(Table(table_data, style=[('GRID', (0,0), (-1,-1), 1, colors.black)]))
                    elements.append(Spacer(1, 12))


                resumen_data = [['Método', 'Matriz', 'Iteraciones']]

                for metodo, datos in resultados.items():
                    try:
                        tabla = pd.read_html(datos['tabla'])[0]
                        
                        solucion = datos["solucion"]
                        radio = datos["radio"]
                        
                        iteraciones = len(tabla)
                        resumen_data.append([metodo, str(solucion), str(iteraciones)])
                    except Exception as e:
                        resumen_data.append([metodo, 'Error', 'Error'])


                mejor_metodo = None
                menor_iteraciones = float('inf')

                for fila in resumen_data[1:]:   
                    metodo, raiz, iteraciones = fila

                    print(fila)

                    print(fila)
                    try:
                        iteraciones = int(iteraciones)
                        if iteraciones < menor_iteraciones and raiz != 'Error':
                            menor_iteraciones = iteraciones
                            mejor_metodo = metodo
                    except:
                        continue


                elements.append(Spacer(1, 24))
                if mejor_metodo:
                    mensaje_final = f"El mejor método según el menor número de iteraciones es: <b>{mejor_metodo}</b> con {menor_iteraciones} iteraciones."
                else:
                    mensaje_final = "No se pudo determinar un mejor método por errores en los datos."


                        

                elements.append(Spacer(1, 24))
                elements.append(Paragraph("<b>Resumen de raíces e iteraciones</b>", style=None))
                elements.append(Table(resumen_data, style=[('GRID', (0,0), (-1,-1), 1, colors.black)]))

                elements.append(Paragraph(mensaje_final, style=None))

                doc.build(elements)
                buffer.seek(0)
                return FileResponse(buffer, as_attachment=True, filename="resultados.pdf")
            except Exception as e:
                resultado = "Error"
                tabla = [f"Error en los datos: {e}"]

    else:
        form = TodosForm()

    return render(request, 'todosN.html', {'form': form})