from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Categoria,Cliente,Detalleventa,Empleado,Pago,Producto,Tipopago,Venta,Empleado
from django.db.models import Q
from datetime import datetime
from django.contrib import messages
from .forms import PagoForm

##Login-------------------------------------

def signup(request):
    if request.user.is_authenticated:
        return redirect('/signin')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/signin')
        else:
            errors = form.errors
            for field, error in errors.items():
                messages.error(request, f"{field}: {error}")
            return render(request, 'Signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'Signup.html', {'form': form}) 

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'Profile.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile') #profile
        else:
            msg = 'Error Credenciales'
            form = AuthenticationForm(request.POST)
            return render(request, 'Login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'Login.html', {'form': form})
  
def profile(request): 
    return render(request, 'Profile.html')
   
def signout(request):
    logout(request)
    return redirect('/profile')

##Productos--------------------------------

def productos(request):
    productos=Producto.objects.all()
    categorias=Categoria.objects.all()
    context = {'productos': productos,
               'categorias':categorias}
    return render(request, 'RegistrarProducto.html', context)

def listarproductos(request):
    producto_list=Producto.objects.all()
    context={"productos":producto_list}
    return render(request,"RegistrarProducto.html",context)

def registrarproductos(request):
    idProducto=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    precio=request.POST["txtprecio"]
    stock=request.POST["txtstock"]
    descripcion=request.POST["txtdescripcion"]
    id_Categoria = request.POST["txtcategoria"]
    categoria=Categoria.objects.get(idCategoria=id_Categoria)
    
    producto=Producto.objects.create(idProducto=idProducto,
                nombre=nombre,precio=precio,idCategoria=categoria,stock=stock,descripcion=descripcion)
    return redirect('/producto')

def eliminarproductos(request,id):
    producto=Producto.objects.get(id=id)
    producto.delete()
    return redirect('/producto')

def editarproductos(request,idProducto):
    producto=Producto.objects.get(idProducto=idProducto)
    producto_list=Producto.objects.all()
    categoria=Categoria.objects.all()
    context={'producto':producto,
            'productos':producto_list,     
            'categorias':categoria
        }
    return render(request,"EditarProducto.html",context)

def buscarproductos(request):
    buscar_producto=request.POST.get("buscar")
    productos=Producto.objects.all()
    if buscar_producto:
        productos=Producto.objects.filter(
            Q(nombre__icontains=buscar_producto)
        ).distinct()

    datos={
        'productos':productos
    }
    return render(request,'ListaProductos.html',datos)


# VENTAS--------------------------------
def listadoventa(request):
    venta_list = Venta.objects.all()
    return render(request, "VentaRegistro.html", {"ventas": venta_list})


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


# ---------------------PAGO--------------


def listado_pago(request):
    pagos = Pago.objects.all()
    return render(request, 'pago_registrar.html', {"pagos": pagos})


def registrar_pago(request):
    if request.method == 'POST':
        numero_tarjeta = request.POST.get('numero_tarjeta')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')
        id_tipo = request.POST.get('tpago')
        cvc = request.POST.get('cvc')

        # Realiza la lógica de validación y creación del objeto Pago
        # Puedes agregar más validaciones según tus necesidades

        tipo_pago = Tipopago.objects.get(idTipopago=id_tipo)
        pago = Pago(numero_tarjeta=numero_tarjeta,
                    fecha_vencimiento=fecha_vencimiento, tipo_pago=tipo_pago, cvc=cvc)
        pago.save()

        # Redirige a la página de listado de pagos
        return redirect('pagos')

    # Si la solicitud no es POST, renderiza el formulario de registro de pago
    tpagos = Tipopago.objects.all()
    return render(request, 'pago_registrar.html', {'tpagos': tpagos})






def editar_pago(request, idPago):
    pago = get_object_or_404(Pago, idPago=idPago)
    if request.method == 'POST':
        form = PagoForm(request.POST, instance=pago)
        if form.is_valid():
            form.save()
            return redirect('listado_pago')
    else:
        form = PagoForm(instance=pago)
    return render(request, 'pago_editar.html', {'form': form, 'pago': pago})


def eliminar_pago(request, idPago):
    pago = get_object_or_404(Pago, idPago=idPago)
    pago.delete()
    return redirect('listado_pago')


# ---------------------CLIENTES-------------

def clientes(request):
    cliente_list = Cliente.objects.all()
    return render(request, "ClienteListado.html", {"clientes": cliente_list})


def listado_cliente(request):
    cliente_list = Cliente.objects.all()
    return render(request, "ClienteRegistro.html", {"clientes": cliente_list})

def registrarcliente(request):
    if request.method == "POST":
        nombres = request.POST.get("nombres")
        apellidos = request.POST.get("apellidos")
        dni = request.POST.get("dni")
        direccion = request.POST.get("direccion")
        telefono = request.POST.get("telefono")
        correo = request.POST.get("correo")

        cliente = Cliente.objects.create(
            nombres=nombres,
            apellidos=apellidos,
            dni=dni,
            dirección=direccion,
            teléfono=telefono,
            correo=correo
        )

        return render(
            request,
            'ClienteRegistro.html',
            {"cliente": cliente}
        )
    else:
        return render(
            request,
            "ClienteRegistro.html"
        )


def eliminar_cliente(request, idCliente):
    cliente = Cliente.objects.get(idCliente=idCliente)
    cliente.delete()
    return redirect('/clientes/')


def  editar_cliente(request, idCliente):
    cliente = get_object_or_404(Cliente, idCliente=idCliente)

    if request.method == 'POST':
        nombres = request.POST["nombres"]
        apellidos = request.POST["apellidos"]
        dni = request.POST["dni"]
        direccion = request.POST["direccion"]
        telefono = request.POST["telefono"]
        correo = request.POST["correo"]

        cliente.nombres = nombres
        cliente.apellidos = apellidos
        cliente.dni = dni
        cliente.dirección = direccion
        cliente.teléfono = telefono
        cliente.correo = correo

        cliente.update(nombres = nombres,apellidos = apellidos,dni = dni,dirección = direccion,teléfono = telefono,correo = correo)
        return redirect('/')

    return render(request, 'ClienteEditar.html', {'cliente': cliente})







