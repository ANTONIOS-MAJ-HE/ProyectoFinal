from django.urls import path
from . import views


app_name = 'ventas'
urlpatterns = [

    ##Login--------------------------------------
    path('', views.homes, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),

    ##Producto-----------------------------------------
    path('dataproducto/',views.listarproductos,name='listarproductos'),
    path('registrarproducto',views.registrarproductos,name='registrarproducto'),
    path('productos', views.productos, name='productos'),
    path('editarproducto/<str:idProducto>/', views.editarproductos, name='editarproducto'),
    
    ##Ventas-------------------------------------------------
    path('dtventas/', views.listadoventa, name='dtventas'),
    path('registrarventa/', views.registrarventa, name='registrarventa'),
    path('dtventas/eliminarventa/<idVenta>', views.eliminarventa),
    path('dtventas/editarventa/<int:id_venta>', views.editar_venta, name='editar_venta'),

    ##Pagos--------------------------------------------------
    path('pagos/', views.listado_pago, name='pagos'),
    path('pagos/registrar/', views.registrar_pago, name='registrar_pago'),
    path('pagos/eliminar/<int:idPago>/',
         views.eliminar_pago, name='eliminar_pago'),
    path('pagos/editar/<int:id_pago>/', views.editar_pago, name='editar_pago'),
]
