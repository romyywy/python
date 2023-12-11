from django.urls import path

from Productos.views import hello,crear_producto,crear_cliente,crear_vendedor,pag_principal,pag_base


#intentar importar todo de una con from playground import views

urlpatterns = [
    path('hello/',hello),
    path('crear_producto/',crear_producto),
    path('crear_cliente/',crear_cliente),
    path('crear_vendedor/',crear_vendedor),
    path('pag_principal/',pag_principal),
    path('pag_base/',pag_base),
    

]

