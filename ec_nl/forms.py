from django import forms

class PuntoFijoForm(forms.Form):
    X0 = forms.FloatField(label='Valor Inicial X0')
    Tol = forms.FloatField(label='Tolerancia')
    Niter = forms.IntegerField(label='Número de Iteraciones')
    Fun = forms.CharField(label='Función f(x)', max_length=100)
    g = forms.CharField(label='Función g(x)', max_length=100)
