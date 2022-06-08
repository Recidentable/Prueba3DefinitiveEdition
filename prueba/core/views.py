from django.shortcuts import render, redirect
from django.template import loader
from .models import Producto
from .forms import ProductoForm

# Create your views here.
def Jardineria(request):
    return render(request, 'core/Jardineria.html')

def Fertilizantes(request):
    producto = Producto.objects.all()
    datos = {
        'productos': producto
    }
    return render(request, 'core/Fertilizantes.html',datos)

def Maceteros(request):
    producto = Producto.objects.all()
    datos = {
        'productos': producto
    }
    return render(request, 'core/Maceteros.html',datos)

def Flores(request):
    producto = Producto.objects.all()
    datos = {
        'productos': producto
    }
    return render(request, 'core/Flores.html',datos)

def registro_usuario(request):
    return render(request, 'core/registro_usuario.html')

def Tienda(request):
    producto = Producto.objects.all()
    datos = {
        'productos': producto
    }
    return render(request, 'core/Tienda.html',datos)
    

def home(request):
    producto = Producto.objects.all()
    datos = {
        'productos': producto
    }
    return render(request, 'core/home.html', datos)

def form_producto(request):
    datos = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Productos guardados correctamente"
    return render(request, 'core/form_producto.html', datos)

def form_mod_producto(request, id):
    producto = Producto.objects.get(Id=id)
    datos = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Productos modificados correctamente"
    return render(request, 'core/form_mod_producto.html', datos)

def form_del_producto(request, id):
    producto = Producto.objects.get(Id=id)
    producto.delete()
    return redirect(to="home")
