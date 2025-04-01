from django import forms

class BiseccionForm(forms.Form):
    a = forms.FloatField(label='Valor Inicial intervalo')
    b = forms.FloatField(label='Valor final intervalo')
    tol = forms.FloatField(label='Tolerancia')
    niter = forms.IntegerField(label='Número de Iteraciones')
    fun = forms.CharField(label='Función f(x)', max_length=100)


class RaicesMultiplesForm(forms.Form):
    X0 = forms.FloatField(label="Valor inicial X₀")
    Tol = forms.FloatField(label="Tolerancia")
    Niter = forms.IntegerField(label="Número máximo de iteraciones")
    Fun = forms.CharField(label="Función f(x)", max_length=100)
    df = forms.CharField(label="Derivada f'(x)", max_length=100)
    ddf = forms.CharField(label="Segunda derivada f''(x)", max_length=100)


class PuntoFijoForm(forms.Form):
    X0 = forms.FloatField(label='Valor Inicial X0')
    Tol = forms.FloatField(label='Tolerancia')
    Niter = forms.IntegerField(label='Número de Iteraciones')
    Fun = forms.CharField(label='Función f(x)', max_length=100)
    g = forms.CharField(label='Función g(x)', max_length=100)


class NewtonForm(forms.Form):
    X0 = forms.FloatField(label='Valor Inicial X0')
    Tol = forms.FloatField(label='Tolerancia')
    Niter = forms.IntegerField(label='Número de Iteraciones')
    Fun = forms.CharField(label='Función f(x)', max_length=100)
    df_expr = forms.CharField(label='Función df_expr(x)', max_length=100)


