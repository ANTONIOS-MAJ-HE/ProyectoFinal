from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Categoria,Cliente,Detalleventa,Empleado,Pago,Producto,Tipopago,Venta
from django.db.models import Q
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

