from django import forms

class BiseccionForm(forms.Form):
    modo_opciones = [
        ('cs', 'Cifras Significativas'),
        ('dc', 'Decimales Correctos')
    ]

    a = forms.FloatField(label='Valor Inicial intervalo')
    b = forms.FloatField(label='Valor final intervalo')
    tol = forms.FloatField(label='Tolerancia')
    niter = forms.IntegerField(label='Número de Iteraciones')
    fun = forms.CharField(label='Función f(x)', max_length=100)
    Modo = forms.ChoiceField(choices=modo_opciones, label="Modo")


class RaicesMultiplesForm(forms.Form):
    modo_opciones = [
        ('cs', 'Cifras Significativas'),
        ('dc', 'Decimales Correctos')
    ]

    X0 = forms.FloatField(label="Valor inicial X₀")
    Tol = forms.FloatField(label="Tolerancia")
    Niter = forms.IntegerField(label="Número máximo de iteraciones")
    Fun = forms.CharField(label="Función f(x)", max_length=100)
    df = forms.CharField(label="Derivada f'(x)", max_length=100)
    ddf = forms.CharField(label="Segunda derivada f''(x)", max_length=100)
    Modo = forms.ChoiceField(choices=modo_opciones, label="Error")


class PuntoFijoForm(forms.Form):

    modo_opciones = [
        ('cs', 'Cifras Significativas'),
        ('dc', 'Decimales Correctos')
    ]

    X0 = forms.FloatField(label='Valor Inicial X0')
    Tol = forms.FloatField(label='Tolerancia')
    Niter = forms.IntegerField(label='Número de Iteraciones')
    Fun = forms.CharField(label='Función f(x)', max_length=100)
    g = forms.CharField(label='Función g(x)', max_length=100)
    Modo = forms.ChoiceField(choices=modo_opciones, label="Error")

class NewtonForm(forms.Form):

    modo_opciones = [
        ('cs', 'Cifras Significativas'),
        ('dc', 'Decimales Correctos')
    ]

    X0 = forms.FloatField(label='Valor Inicial X0')
    Tol = forms.FloatField(label='Tolerancia')
    Niter = forms.IntegerField(label='Número de Iteraciones')
    Fun = forms.CharField(label='Función f(x)', max_length=100)
    df_expr = forms.CharField(label='Derivada de la función f(x)', max_length=100)
    Modo = forms.ChoiceField(choices=modo_opciones, label="Error")

class ReglaFalsaForm(forms.Form):

    modo_opciones = [
        ('cs', 'Cifras Significativas'),
        ('dc', 'Decimales Correctos')
    ]

    a = forms.FloatField(label='Valor inicial del intervalo a.')
    b = forms.FloatField(label='Valor final del intervalo b.')
    Tol = forms.FloatField(label='Tolerancia')
    Niter = forms.IntegerField(label='Número de Iteraciones')
    Fun = forms.CharField(label='Función f(x)', max_length=100)
    Modo = forms.ChoiceField(choices=modo_opciones, label="Error")

class SecanteForm(forms.Form):

    modo_opciones = [
        ('cs', 'Cifras Significativas'),
        ('dc', 'Decimales Correctos')
    ]

    X0 = forms.FloatField(label='Valor inicial X0.')
    X1 = forms.FloatField(label='Valor final X1.')
    Tol = forms.FloatField(label='Tolerancia')
    Niter = forms.IntegerField(label='Número de Iteraciones')
    Fun = forms.CharField(label='Función f(x)', max_length=100)
    Modo = forms.ChoiceField(choices=modo_opciones, label="Error")


class todosForm(forms.Form):
    modo_opciones = [
        ('cs', 'Cifras Significativas'),
        ('dc', 'Decimales Correctos')
    ]

    a = forms.FloatField(label='Valor Inicial intervalo')
    b = forms.FloatField(label='Valor final intervalo')
    tol = forms.FloatField(label='Tolerancia')
    niter = forms.IntegerField(label='Número de Iteraciones')
    fun = forms.CharField(label='Función f(x)', max_length=100)
    df = forms.CharField(label="Derivada f'(x)", max_length=100)
    ddf = forms.CharField(label="Segunda derivada f''(x)", max_length=100)
    g = forms.CharField(label='Función g(x)', max_length=100)
    Modo = forms.ChoiceField(choices=modo_opciones, label="Error")



