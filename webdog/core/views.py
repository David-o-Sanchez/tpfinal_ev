from django.shortcuts import render, HttpResponse

# Create your views here.

def historia(request):
    return render(request, "core/historia.html")

def quienes(request):
    return render(request, "core/quienes.html")

def guarderia(request):
    return render(request, "core/guarderia.html")

def contactos(request):
    return render(request, "core/contactos.html")

def inicio(request):
    return render(request, "core/inicio.html")