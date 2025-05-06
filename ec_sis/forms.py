from django import forms

class JacobiForm(forms.Form):
    A = forms.CharField(label='Matriz A', widget=forms.Textarea(attrs={'rows': 3}))
    b = forms.CharField(label='Vector b')
    x0 = forms.CharField(label='Vector inicial x0')
    tol = forms.FloatField(label='Tolerancia', initial=1e-5)
    niter = forms.IntegerField(label='Máximo de iteraciones', initial=100)