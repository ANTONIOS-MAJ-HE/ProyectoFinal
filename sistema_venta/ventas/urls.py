from django.urls import path
from . import views


app_name = 'ventas'
urlpatterns = [

    path('', views.homes, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
<<<<<<< HEAD

    ##Producto-----------------------------------------
    path('dataproducto/',views.listarproductos,name='listarproductos'),
    ##path('producto/',views.buscarproductos,name='home'),
    path('registrarproducto',views.registrarproductos,name='registrarproducto'),
    path('productos', views.productos, name='productos'),
    path('editarproducto/<str:idProducto>/', views.editarproductos, name='editarproducto'),
=======
    path('dtventas/', views.listadoventa, name='dtventas'),
    path('registrarventa/', views.registrarventa, name='registrarventa'),
    path('dtventas/eliminarventa/<idVenta>', views.eliminarventa),
    path('dtventas/editarventa/<int:id_venta>', views.editar_venta, name='editar_venta'),
>>>>>>> 9926fc613d0dfa3f5af3b6be0c6a65a33868d1e1
]