from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect



def index(request):
    return render(request, "index.html")

def metodos(request):

    if request.method == "GET":
        return render(request, "metodos.html")
    if request.method == "POST":
        print("hello0")
        return redirect("/biseccion/")

def acerca_de(request):
    return render(request, "acerca_de.html")
    
def biseccion(request):
    return render(request, "biseccion.html")

def regla_falsa(request):
    return render(request, "regla_falsa.html")

def punto_fijo(request):
    return render(request, "punto_fijo.html")

def newton(request):
    return render(request, "newton.html")

def secante(request):
    return render(request, "secante.html")

def raices_multiples(request):
    return render(request, "raices_multiples.html")
