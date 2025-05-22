from django.shortcuts import render
from .forms import VanderForm
from .metodos.vander import vandermonde
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

            resultado = {
                'solucion': pol,
                'grafica': grafica,
            }            

            return render(request, 'result_vander.html', {'form': form, 'resultado': resultado, 'grafica': grafica})
    else:
        form = VanderForm()

    return render(request, 'vander.html', {'form': form})