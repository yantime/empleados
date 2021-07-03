from django.shortcuts import redirect, render,HttpResponse
from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.
def home(request):
    empleados=Empleado.objects.all()  # select * from empleados
    contexto={"empleados":empleados}
    return render(request,"apps/home.html",contexto)

def agregar(request):
    if request.method=="POST":
        form=EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=EmpleadoForm()
    contexto={"form":form}
    return render(request,"apps/agregar.html",contexto)

def eliminar(request,empleado_id):
    empleado=Empleado.objects.get(id=empleado_id) # select * from empleado where id=2
    empleado.delete()
    return redirect('home')

def editar(request,empleado_id):
    empleado=Empleado.objects.get(id=empleado_id) # select * from empleado where id=2
    if request.method=="POST":
        form=EmpleadoForm(request.POST,instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=EmpleadoForm(instance=empleado)
    contexto={"form":form}
    return render(request,"apps/editar.html",contexto)