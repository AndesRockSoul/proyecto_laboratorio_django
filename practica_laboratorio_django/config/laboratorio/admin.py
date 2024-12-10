from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto
# Register your models here.

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    list_display_links = ['nombre']
   # list_filter = ('nombre') #lo apague porque no se puede filtrar x 1 
   
   
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'laboratorio')
    list_display_links = ['nombre', ]
    list_filter = ('nombre', 'laboratorio') 
    
  #  def laboratorio_nombre(self,obj):
   #     return obj.laboratorio.nombre if obj.laboratorio else '-'
   # laboratorio_nombre.short_description = 'Laboratorio'
    
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'fecha_fabricacion','p_costo','p_venta')
    list_display_links = ['nombre']
    list_filter = ('nombre', 'laboratorio') 

#def laboratorio_nombre(self, obj):
#        return obj.laboratorio.nombre if obj.laboratorio else '-'
#laboratorio_nombre.short_description = 'Laboratorio' 

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)