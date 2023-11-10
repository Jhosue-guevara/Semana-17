from django.urls import path
from .views import agregar_cliente, lista_clientes,agregar_area,agregar_empleado,lista_empleados,lista_areas,agregar_venta,lista_ventas

urlpatterns = [
    path('agregar_cliente/', agregar_cliente, name='agregar_cliente'),
    path('lista_clientes/', lista_clientes, name='lista_clientes'),
     path('agregar_area/', agregar_area, name='agregar_area'),
    path('agregar_empleado/', agregar_empleado, name='agregar_empleado'),
    path('lista_empleados/', lista_empleados, name='lista_empleados'),
    path('lista_areas/', lista_areas, name='lista_areas'),
    path('agregar_venta/', agregar_venta, name='agregar_venta'),
    path('lista_ventas/', lista_ventas, name='lista_ventas'),


]
