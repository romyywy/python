from django.shortcuts import render
from django.http import HttpResponse
from Productos.models import Product,Cliente,Vendedor
#este no se para que es: from django.template import loader

# Create your views here.

#view de prueba
def hello(request):
    #return HttpResponse('hello')
    return render(request,'hello.html')


#form para productos


def crear_producto(request):
    if request.method =="POST":
        nuevo_producto = Product(
            nombre=request.POST["nombre"],
            descripcion=request.POST["descripcion"],
            cantidad_stock=request.POST["cantidad_stock"],
        )
        nuevo_producto.save()
        return render(request, "index.html")
    return render(request,'product_formulario.html')



#form para clientes

def crear_cliente(request):
    if request.method =="POST":
        nuevo_cliente = Cliente(
            nombre=request.POST["nombre"],
            correo=request.POST["correo"],
        )
        nuevo_cliente.save()
        return render(request, "index.html")
    return render(request,'cliente_formulario.html')


#form para vendedor
def crear_vendedor(request):
    if request.method =="POST":
        nuevo_vendedor=Vendedor(
            nombre=request.POST["nombre"],
            tienda=request.POST["tienda"],
        )
        nuevo_vendedor.save()
        return render(request, "index.html")
    return render(request,'vendedor_formulario.html')
    

#para pag index

def pag_principal(request):
    return render(request,"index.html")    

#para pag base
def pag_base(request):
    return render(request,"base.html")    
