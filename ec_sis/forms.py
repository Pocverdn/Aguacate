from django import forms

class JacobiForm(forms.Form):
    A = forms.CharField(label='Matriz A', widget=forms.Textarea(attrs={'rows': 3, 'placeholder':'Ejemplo:\n1 2 3\n4 5 6\n7 8 9'}))
    b = forms.CharField(label='Vector b')
    x0 = forms.CharField(label='Vector inicial x0')
    tol = forms.FloatField(label='Tolerancia', initial=1e-5)
    niter = forms.IntegerField(label='Máximo de iteraciones', initial=100)

class GausseidelForm(forms.Form):
    A = forms.CharField(label='Matriz A', widget=forms.Textarea(attrs={'rows': 3, 'placeholder':'Ejemplo:\n1 2 3\n4 5 6\n7 8 9'}))
    b = forms.CharField(label='Vector b')
    x0 = forms.CharField(label='Vector inicial x0')
    tol = forms.FloatField(label='Tolerancia', initial=1e-5)
    niter = forms.IntegerField(label='Máximo de iteraciones', initial=100)