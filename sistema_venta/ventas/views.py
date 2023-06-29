from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Venta, Empleado, Cliente
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
# Create your views here.

def homes(request): 
    return render(request, 'Home.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'Signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'Signup.html', {'form': form})
   
def homes(request): 
    return render(request, 'Home.html')
   
  
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'Home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'Login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'Login.html', {'form': form})
  
def profile(request): 
    return render(request, 'Profile.html')
   
def signout(request):
    logout(request)
    return redirect('/')


# ListadoVenta
def listadoventa(request):
    venta_list = Venta.objects.all()
    return render(request, "VentaListado.html", {"ventas": venta_list})


def registrarventa(request):
    if request.method == 'POST':
        codigo = request.POST['txtcodigo']
        fecha = request.POST['txtfecha']
        subtotal = request.POST['txtsubtotal']
        igv = request.POST['txtigv']
        monto = request.POST['txtmonto']
        id_cliente = request.POST['cliente']
        id_empleado = request.POST['empleado']

        cliente = Cliente.objects.get(pk=id_cliente)
        empleado = Empleado.objects.get(pk=id_empleado)

        venta = Venta(
            idVenta=codigo,
            fecha=fecha,
            subtotal=subtotal,
            igv=igv,
            monto=monto,
            idcliente=cliente,
            idempleado=empleado
        )
        venta.save()

        # Redirige a la página de listado de ventas
        return redirect('ventas:dtventas')

    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()

    return render(request, 'VentaRegistro.html', {'clientes': clientes, 'empleados': empleados})


def eliminarventa(request, idVenta):

    venta = Venta.objects.get(idVenta=idVenta)
    venta.delete()
    return redirect('/dtventas/')


def editar_venta(request, id_venta):
    venta = get_object_or_404(Venta, idVenta=id_venta)
    empleados = Empleado.objects.all()
    clientes = Cliente.objects.all()

    if request.method == 'POST':
        # Obtener los datos del formulario
        id_cliente = request.POST.get('id_cliente')
        id_empleado = request.POST.get('id_empleado')
        fecha = request.POST.get('fecha')
        subtotal = request.POST.get('subtotal')
        igv = request.POST.get('igv')
        monto = request.POST.get('monto')
# Convertir la fecha al formato correcto
        fecha = datetime.strptime(fecha, '%B %d, %Y').strftime('%Y-%m-%d')


        # Obtener las instancias de Cliente y Empleado
        cliente = get_object_or_404(Cliente, idCliente=id_cliente)
        empleado = get_object_or_404(Empleado, idEmpleado=id_empleado)

        # Actualizar los campos de la venta
        venta.idcliente = cliente
        venta.idempleado = empleado
        venta.fecha = fecha
        venta.subtotal = subtotal
        venta.igv = igv
        venta.monto = monto

        # Guardar los cambios en la venta
        venta.save()

        # Redireccionar a una página de éxito o a la página de detalles de la venta
        return redirect('/dtventas/', id_venta=venta.idVenta)

    return render(request, 'VentaEditar.html', {'venta': venta, 'empleados': empleados, 'clientes': clientes})
# BUSCAR-----------------


def buscarespecialidad(request):
    buscar_especialidad = request.POST.get("buscar")
    especialidades = Especialidad.objects.all()

    if buscar_especialidad:
        especialidades = Especialidad.objects.filter(
            Q(nombre__icontains=buscar_especialidad)
        ).distinct()
    datos = {
        'especialidades': especialidades
    }
    return render(request, 'ListaEspecialidad.html', datos)
