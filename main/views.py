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
        return redirect("/metodo1/")
    
def metodo1(request):
    return render(request, "metodo1.html")

def metodo2(request):
    return render(request, "metodo2.html")