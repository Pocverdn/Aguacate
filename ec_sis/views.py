from django.shortcuts import render

from .forms import JacobiForm
from .metodos import jacobi 

import numpy as np

def jacobi_view(request):
    resultado = None
    errores = None

    if request.method == 'POST':
        form = JacobiForm(request.POST)
        if form.is_valid():
            try:
                A = np.array(eval(form.cleaned_data['A']))
                b = np.array(eval(form.cleaned_data['b']))
                x0 = np.array(eval(form.cleaned_data['x0']))
                tol = form.cleaned_data['tol']
                niter = form.cleaned_data['niter']

                errores, solucion = jacobi(x0, A, b, tol, niter)
                resultado = {
                    'solucion': solucion,
                    'errores': errores,
                }
            except Exception as e:
                resultado = None
                errores = [f"Error en los datos: {e}"]
    else:
        form = JacobiForm()

    return render(request, 'jacobi.html', {'form': form, 'resultado': resultado, 'errores': errores})