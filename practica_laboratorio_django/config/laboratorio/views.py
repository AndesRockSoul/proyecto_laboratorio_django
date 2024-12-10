from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages 
from django.urls import reverse
from django.shortcuts import render
from .models import Producto, Laboratorio
from .forms import ProductoForm, LaboratorioForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listar(request):
    productos= Producto.objects.using('default').all().order_by('id')
    return render(request,  'listar_productos.html', {'productos':productos})

def listar_laboratorios(request):
    laboratorios = Laboratorio.objects.using('default').all().order_by('id')
    nro_visitas = request.session.get('nro_visitas', 0)
    nro_visitas += 1
    request.session['nro_visitas'] = nro_visitas
    return render(request, 'listar_laboratorios.html', {'laboratorios':laboratorios,'nro_visitas':nro_visitas})

def crear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Producto creado exitosamente')
            return redirect('listar')
        else:
            messages.error(request, 'Revisar datos ingresados')
            return render(request, 'crear_producto.html',{'producto_form':form})
    else:
        form = ProductoForm()
        return render(request, 'crear_producto.html',{'producto_form':form})
    
def crear_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Laboratorio creado exitosamente')
            return redirect('listar_laboratorios')
        else:
            messages.error(request, 'Revisar datos ingresados')
            return render(request, 'crear_laboratorio.html',{'laboratorio_form':form})
    else:
        form = LaboratorioForm()
        return render(request, 'crear_laboratorio.html',{'laboratorio_form':form})    
    
def editar(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save() 
            producto.save()
            messages.success(request, 'Producto editado exitosamente')
            return redirect('listar')
        else:
            messages.error(request, 'Revisar datos ingresados')
            return HttpResponseRedirect(reverse('editar', args=[producto.id]))
    else:
        form = ProductoForm(instance=producto)
        return render(request, 'editar_producto.html',{'form':form, 'producto_id':producto_id})
    
def editar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, pk=laboratorio_id)
    
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            laboratorio = form.save() 
            laboratorio.save()
            messages.success(request, 'laboratorio editado exitosamente')
            return redirect('listar_laboratorios')
        else:
            messages.error(request, 'Revisar datos ingresados')
            return HttpResponseRedirect(reverse('editar_laboratorio', args=[laboratorio.id]))
    else:
        form = LaboratorioForm(instance=laboratorio)
        return render(request, 'editar_laboratorio.html',{'form':form, 'laboratorio_id':laboratorio_id}) 

def eliminar(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id) 
    producto.delete()
    messages.info(request, 'Producto eliminado correctamente') 
    return redirect('listar')  


def eliminar_laboratorio(request, laboratorio_id):
    laboratorio = get_object_or_404(Laboratorio, id=laboratorio_id) 
    if laboratorio is None or not laboratorio.id:
        raise Http404("Laboratorio no existe")
    
    if request.method == 'POST':
        laboratorio.delete()
        messages.success(request, 'laboratorio eliminado correctamente') 
        return redirect('listar_laboratorios') 
    return render(request,'eliminar_laboratorio.html',{'laboratorio':laboratorio})

