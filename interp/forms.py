from django import forms

class VanderForm(forms.Form):
    x = forms.CharField(label='Puntos en x')
    y = forms.CharField(label='Puntos en y')
    grado = forms.IntegerField(label='Grado')
