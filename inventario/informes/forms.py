from django import forms
from .models import Aplicaciones, Prestamo, Empleado

class PrestamoForm(forms.ModelForm):
            
    class Meta:
        model = Prestamo
        fields = ('empleado','Dispositivo','Identificador','Marca','Modelo','CPU','RAM','Almacenamiento','NumeroSerie','Observaciones','FechaInicio','FechaDevolucion')
        widgets = {
            'FechaInicio' : forms.SelectDateWidget(
                attrs={
                    
                }
            ),
            'FechaDevolucion' : forms.SelectDateWidget(),
            'Identificador':forms.TextInput(attrs={
                'placeholder':'Nombre o numero de telefono',
                'style':'width: 5cm'
            }),

            'Marca':forms.TextInput(attrs={
                'placeholder':'Marca del dispositivo',
                'style':'width: 5cm'
            }),

            'Modelo':forms.TextInput(attrs={
                'placeholder':'Modelo del dispositivo',
                'style':'width: 5cm'
            }),

            'CPU':forms.TextInput(attrs={
                'placeholder':'Procesador del dispositivo',
                'style':'width: 5cm'
            }),

            'Observaciones':forms.TextInput(attrs={
                'placeholder':'Detalles del prestamo',
                'style':'padding-bottom: 2cm; width: 5cm'
            }),

            'NumeroSerie':forms.TextInput(attrs={
                'placeholder':'Numero de serie',
                'style':'width: 5cm'
            }),

            'RAM':forms.Select(attrs={
                'style':'width: 3cm; text-align:center'
            }),

            'Almacenamiento':forms.Select(attrs={
                'style':'width: 3cm; text-align:center'
            }),

            'empleado':forms.TextInput(attrs={
                'placeholder':'ej. 12345678A',
                'maxlength':9,
                'style':'width: 3cm;'
            }),

            'Dispositivo':forms.Select(attrs={
                'style':'width: 3cm; text-align:center'
            }),
        }

class AppForm(forms.ModelForm):
    class Meta:
        model = Aplicaciones
        fields = ('prestamo','programa','detalles','fecha')
        widgets = {
            'programa':forms.TextInput(attrs={
                'placeholder':'Nombre del programa'
            }),

            'detalles':forms.TextInput(attrs={
                'placeholder':'Detalles de la activación',
                'style':'padding-bottom: 2cm; width: 5cm'
            }),

            'fecha':forms.SelectDateWidget(),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, widget=forms.TextInput(attrs={
        'placeholder':'Nombre de usuario', 
        'style':'padding: 10px;border: 1px solid #ccc; border-radius: 3px; font-size: 16px'
    }))
    password = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={
        'placeholder':'Contraseña', 
        'style':'padding: 10px;border: 1px solid #ccc; border-radius: 3px; font-size: 16px'
    }))
    