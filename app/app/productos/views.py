from django.shortcuts import render

# Create your views here.
def productos(request):
    productos = "azucar"
    return render(request, 'productos.html',{'productos': productos})