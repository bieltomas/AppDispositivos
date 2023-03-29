from django.contrib.auth import login, authenticate, logout
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.template import loader
from .forms import AppForm, LoginForm, PrestamoForm
from .models import Aplicaciones, Prestamo, Empleado


def index(request):
    return render(request, 'informes/index.html')

def prestamos(request):
    if not request.user.is_authenticated:
        return render(request, 'informes/error.html')
    ss = request.GET.get('search')
    lista = Prestamo.objects.order_by('-FechaInicio')[:5]
    listaF = Prestamo.objects.filter(empleado_id = ss).order_by('-FechaInicio') 
    template = loader.get_template('informes/prestamos.html')
    context = {
        'listaF':listaF,
        'lista':lista
    }
    return HttpResponse(template.render(context,request))
    


def prestamo(request, prestamo_id):
    if not request.user.is_authenticated:
        return render(request, 'informes/error.html')
    atributos = Prestamo.objects.values().filter(id=prestamo_id)
    apps = Aplicaciones.objects.values().filter(prestamo=prestamo_id)
    template = loader.get_template('informes/prestamo.html')
    context = {
        'atributos':atributos,'apps':apps,
        
    }
    return HttpResponse(template.render(context,request))

def crear(request):
    if not request.user.is_authenticated:
        return render(request, 'informes/error.html')
    if request.method == "POST":
        prestamo_form = PrestamoForm(request.POST, request.FILES)
        if prestamo_form.is_valid():
            prestamo_form.save()
            messages.success(request, ('Se ha añadido el prestamo correctamente!'))
        else:
            messages.error(request, 'Error guardando el prestamo')

        return redirect("/informes/prestamos")
    prestamo_form = PrestamoForm()
    prestamosA = Prestamo.objects.all()
    return render(request=request, template_name="informes/crear.html", context={'prestamo_form':prestamo_form, 'prestamosA':prestamosA,})

#  if request.method == "POST":
#       app_form = AplicacionesForm(request.POST, request.FILES)
#        if app_form.is_valid():
 #           app_form.save()
 #       else:
 #           messages.error(request, 'Error guardando las apps')
#
#        return redirect("/informes/prestamos")
#    app_form = AplicacionesForm()
#    appsA = Aplicaciones.objects.all()

   
def editar(request, prestamo_id):
    if not request.user.is_authenticated:
        return render(request, 'informes/error.html')
    obj = get_object_or_404(Prestamo, id=prestamo_id)
    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(f'/informes/prestamos/{prestamo_id}')
    else:
        form = PrestamoForm(instance=obj)
        return render(request, 'informes/edit.html', {'form':form, 'obj':obj})


def delete(request, prestamo_id):
    if not request.user.is_authenticated:
        return render(request, 'informes/error.html')
    obj = Prestamo.objects.get(id=prestamo_id)
    
    if request.method == 'POST':
        obj.delete()
        return redirect('prestamos')
    
    return render(request, 'informes/delete.html', {'obj':obj})


def crearB(request, prestamo_id):
    if not request.user.is_authenticated:
        return render(request, 'informes/error.html')
    if request.method == "POST":
        app_form = AppForm(request.POST, request.FILES, initial={'prestamo':Prestamo.objects.get})
        if app_form.is_valid():
            app_form.save()
            messages.success(request, ('Se ha añadido la aplicación correctamente!'))
        else:
            messages.error(request, 'Error guardando la aplicación')
        
        return redirect(f'/informes/prestamos/{prestamo_id}')
    obj = Prestamo.objects.get(id=prestamo_id)
    data = {
        'prestamo': obj
    }
    app_form = AppForm(initial=data)
    appsA = Aplicaciones.objects.all()
    return render(request=request, template_name="informes/crearB.html", context={'app_form':app_form, 'appsA':appsA,})

def deleteB(request, apps_id):
    if not request.user.is_authenticated:
        return render(request, 'informes/error.html')
    obj = Aplicaciones.objects.get(id=apps_id)
    prestamo_id = obj.prestamo.id
    if request.method == 'POST':
        obj.delete()
        return redirect(f'/informes/prestamos/{prestamo_id}')
    
    return render(request, 'informes/deleteB.html', {'obj':obj})

def loginU(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
               return redirect('login')
    return render(request, 'informes/login.html', context={'form':form})

def logoutU(request):
    logout(request)
    return redirect('index')
    

""" class EmpleadoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Empleado.objects.all()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs """