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
    
