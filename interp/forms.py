from django import forms

class VanderForm(forms.Form):
    x = forms.CharField(label='Puntos en x')
    y = forms.CharField(label='Puntos en y')
    grado = forms.IntegerField(label='Grado')

class LagrangeForm(forms.Form):
    x = forms.CharField(label='Puntos en x')
    y = forms.CharField(label='Puntos en y')

class NewtonintForm(forms.Form):
    x = forms.CharField(label='Puntos en x')
    y = forms.CharField(label='Puntos en y')

class SplineLinIntForm(forms.Form):
    x = forms.CharField(label='Puntos en x')
    y = forms.CharField(label='Puntos en y')

class SplineCubIntForm(forms.Form):
    x = forms.CharField(label='Puntos en x')
    y = forms.CharField(label='Puntos en y')


class TodoForm(forms.Form):
    x = forms.CharField(label='Puntos en x')
    y = forms.CharField(label='Puntos en y')
    grado = forms.IntegerField(label='Grado')