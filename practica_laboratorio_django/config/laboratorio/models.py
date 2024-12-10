from django.db import models
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _ 
from django.core.validators import MinValueValidator
from datetime import date
import datetime
from django import forms

# Create your models here.
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50,blank=True, null=True)
    pais = models.CharField(max_length=50,blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ['id']   # anteponiendo el - ej:  -nombre es descendente, asc es predefinido
    
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=50,blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Director General'
        verbose_name_plural = 'Director General'
        ordering = ['id']
    
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField(validators=[MinValueValidator(limit_value=date(2015,1,1))])
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)

    
    def __str__(self):
        return self.nombre
        
    def fecha_fabricacion(self):
        return self.f_fabricacion.year
     
    class Meta:
      #  verbose_name = 'Producto'
       # verbose_name_plural = 'Productos'
        ordering = ['id']   
        

