from django.shortcuts import render, redirect
from .models import cliente,empleado,Area,Ventas
from .forms import ClienteForm ,EmpleadoForm,AreaForm,VentasForm

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes') 
    else:
        form = ClienteForm()

    return render(request, 'agregar_cliente.html', {'form': form})
def agregar_area(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_areas')  # Ajusta el nombre de la vista de inicio
    else:
        form = AreaForm()

    return render(request, 'agregar_area.html', {'form': form})

def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')  # Ajusta el nombre de la vista de inicio
    else:
        form = EmpleadoForm()

    return render(request, 'agregar_empleado.html', {'form': form})
def agregar_venta(request):
    if request.method == 'POST':
        form = VentasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ventas')  # Redirige a la lista de ventas
    else:
        form = VentasForm()
    
    return render(request, 'agregar_venta.html', {'form': form})
def lista_clientes(request):
    clientes = cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})
def lista_empleados(request):
    empleados = empleado.objects.all()
    return render(request, 'lista_empleados.html', {'empleados': empleados})
def lista_areas(request):
    areas = Area.objects.all()
    return render(request, 'lista_areas.html', {'areas': areas})
def lista_ventas(request):
    ventas = Ventas.objects.all()
    return render(request, 'lista_ventas.html', {'ventas': ventas})


