from django import forms

class JacobiForm(forms.Form):

    modo_opciones = [
        ('cs', 'Cifras Significativas'),
        ('dc', 'Decimales Correctos')
    ]

    A = forms.CharField(label='Matriz A', widget=forms.Textarea(attrs={'rows': 3, 'placeholder':'Ejemplo:\n1 2 3\n4 5 6\n7 8 9'}))
    b = forms.CharField(label='Vector b')
    x0 = forms.CharField(label='Vector inicial x0')
    tol = forms.FloatField(label='Tolerancia', initial=1e-5)
    niter = forms.IntegerField(label='Máximo de iteraciones', initial=100)
    Modo = forms.ChoiceField(choices=modo_opciones, label="Error")

class GausseidelForm(forms.Form):

    modo_opciones = [
        ('cs', 'Cifras Significativas'),
        ('dc', 'Decimales Correctos')
    ]
    
    A = forms.CharField(label='Matriz A', widget=forms.Textarea(attrs={'rows': 3, 'placeholder':'Ejemplo:\n1 2 3\n4 5 6\n7 8 9'}))
    b = forms.CharField(label='Vector b')
    x0 = forms.CharField(label='Vector inicial x0')
    tol = forms.FloatField(label='Tolerancia', initial=1e-5)
    niter = forms.IntegerField(label='Máximo de iteraciones', initial=100)
    Modo = forms.ChoiceField(choices=modo_opciones, label="Error")


class TodosForm(forms.Form):

    modo_opciones = [
        ('cs', 'Cifras Significativas'),
        ('dc', 'Decimales Correctos')
    ]
    
    A = forms.CharField(label='Matriz A', widget=forms.Textarea(attrs={'rows': 3, 'placeholder':'Ejemplo:\n1 2 3\n4 5 6\n7 8 9'}))
    b = forms.CharField(label='Vector b')
    x0 = forms.CharField(label='Vector inicial x0')
    tol = forms.FloatField(label='Tolerancia', initial=1e-5)
    w = forms.FloatField(label='w', initial=0.5)
    niter = forms.IntegerField(label='Máximo de iteraciones', initial=100)
    Modo = forms.ChoiceField(choices=modo_opciones, label="Error")

class SORForm(forms.Form):
    modo_opciones = [
        ('cs', 'Cifras Significativas'),
        ('dc', 'Decimales Correctos')
    ]
    A = forms.CharField(label='Matriz A', widget=forms.Textarea(attrs={'rows': 3, 'placeholder':'Ejemplo:\n1 2 3\n4 5 6\n7 8 9'}))
    b = forms.CharField(label='Vector b')
    x0 = forms.CharField(label='Vector inicial x0')
    tol = forms.FloatField(label='Tolerancia', initial=1e-5)
    w = forms.FloatField(label='w', initial=0.5)
    niter = forms.IntegerField(label='Máximo de iteraciones', initial=100)
    Modo = forms.ChoiceField(choices=modo_opciones, label="Error")
    