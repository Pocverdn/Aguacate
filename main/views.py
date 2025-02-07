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

def metodo3(request):
    return render(request, "metodo3.html")

def metodo4(request):
    return render(request, "metodo4.html")

def metodo5(request):
    return render(request, "metodo5.html")

def metodo6(request):
    return render(request, "metodo6.html")

def metodo7(request):
    return render(request, "metodo7.html")

def metodo8(request):
    return render(request, "metodo8.html")

def metodo9(request):
    return render(request, "metodo9.html")

def metodo10(request):
    return render(request, "metodo10.html")

def metodo11(request):
    return render(request, "metodo11.html")

def metodo12(request):
    return render(request, "metodo12.html")

def metodo13(request):
    return render(request, "metodo13.html")

def metodo14(request):
    return render(request, "metodo14.html")

def metodo15(request):
    return render(request, "metodo15.html")

def metodo16(request):
    return render(request, "metodo16.html")

def metodo17(request):
    return render(request, "metodo17.html")

def metodo18(request):
    return render(request, "metodo18.html")

def metodo19(request):
    return render(request, "metodo19.html")

def metodo20(request):
    return render(request, "metodo20.html")

def metodo21(request):
    return render(request, "metodo21.html")

def metodo22(request):
    return render(request, "metodo22.html")

def metodo23(request):
    return render(request, "metodo23.html")

def metodo24(request):
    return render(request, "metodo24.html")