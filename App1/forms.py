from django import forms
from .models import cliente,empleado,Area,Ventas

# Formulario para el modelo Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['nombre', 'Apellido', 'Edad']
# Formulario para el modelo Area
class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['Nombre_del_Area', 'Descripcion']
# Formulario para el modelo Empleado
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = empleado
        fields = ['Nombre', 'Apellido', 'Edad', 'Areaid']
# Formulario para el modelo Ventas
class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = ['Fecha', 'Monto', 'Clienteid', 'Empleadoid']
        widgets = {
            'Fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'Clienteid': forms.Select(attrs={'class': 'form-control'}),
            'Empleadoid': forms.Select(attrs={'class': 'form-control'}),
        }         

