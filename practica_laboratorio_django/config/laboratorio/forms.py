from django.utils import timezone
from django import forms
from .models import Producto, Laboratorio, DirectorGeneral
from django.contrib.auth.forms import UserCreationForm

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['nombre','ciudad','pais']
        labels = {
            'nombre':'Nombre del Laboratorio',
            'ciudad':'Ciudad del Laboratorio',
            'pais':'Pais del Laboratorio',
        }
        widgets = {
            #'laboratorio' : forms.ModelChoiceField(
             #   queryset=Laboratorio.objects.all(),
              #  widget=forms.Select(attrs={'class':'form-control'}))
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'ciudad' : forms.TextInput(attrs={'class':'form-control'}),
            'pais' : forms.TextInput(attrs={'class':'form-control'}),
        }
        
class DirectorGeneral(forms.ModelForm):
    class Meta:
        model = DirectorGeneral
        fields = ['nombre','laboratorio','especialidad']
        labels = {
            'nombre':'Nombre del DirectorGeneral',
            'laboratorio':'laboratorio del DirectorGeneral',
            'especialidad':'especialidad del DirectorGeneral',
        }
        widgets = {
            'nombre' : forms.TextInput(
                attrs={'class':'form-control'}),
            'laboratorio' : forms.TextInput(
                attrs={'class':'form-control'}),
            'especialidad' : forms.TextInput(
                attrs={'class':'form-control'}),
        }
        
        
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'laboratorio', 'f_fabricacion','p_costo', 'p_venta']
        labels = {
           'nombre':'Nombre del Producto',
           'laboratorio':'laboratorio del Producto',
           'f_fabricacion':'fecha de fabricacion del Producto',
           'p_costo':'precio de costo del Producto',
           'p_venta':'precio de venta del producto'
           
        } 
       
        widgets = {
            'nombre' : forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del producto',
                    'required':True
                }),
             'laboratorio': forms.Select(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el laboratorio',
                    'required':True
                }),
            'f_fabricacion' : forms.SelectDateWidget(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'YYYY-MM-DD', 
        }),
            
            'p_costo' : forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el precio de costo',
                    'required':True
        }),
            'p_venta' : forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el precio de venta',
                    'required':True
        })
                
        }
