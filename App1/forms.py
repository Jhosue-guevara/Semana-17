from django import forms
from .models import cliente,empleado,Area,Ventas
class ClienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['nombre', 'Apellido', 'Edad']

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['Nombre_del_Area', 'Descripcion']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = empleado
        fields = ['Nombre', 'Apellido', 'Edad', 'Areaid']

class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = ['Fecha', 'Monto', 'Clienteid', 'Empleadoid']
        widgets = {
            'Fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'Clienteid': forms.Select(attrs={'class': 'form-control'}),
            'Empleadoid': forms.Select(attrs={'class': 'form-control'}),
        }         

