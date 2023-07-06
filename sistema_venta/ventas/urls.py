from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required
from .views import EmpleadoListView

app_name = 'ventas'
urlpatterns = [

    ##Login--------------------------------------
    
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('', views.profile, name='profile'),
    path('signout/', views.signout, name='signout'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='Profile.html'), name='profile'),
    
    ##Producto--------------------------------------

    path('dataproducto/', login_required(views.listarproductos), name='listarproductos'),
    path('registrarproducto/', login_required(views.registrarproductos), name='registrarproducto'),
    path('productos/', login_required(views.productos), name='productos'),
    path('editarproducto/<str:idProducto>/', login_required(views.editarproductos), name='editarproducto'),
    
    ##ventas--------------------------------------
    
    path('dtventas/', login_required(views.listadoventa), name='dtventas'),
    path('registrarventa/', login_required(views.registrarventa), name='registrarventa'),
    path('dtventas/eliminarventa/<idVenta>/', login_required(views.eliminarventa), name='eliminarventa'),
    path('dtventas/editarventa/<int:id_venta>/', login_required(views.editar_venta), name='editar_venta'),

    ##pagos--------------------------------------
    
    path('pagos/', login_required(views.listado_pago), name='pagos'),
    path('pagos/registrar/', login_required(views.registrar_pago), name='registrar_pago'),
    path('pagos/eliminar/<int:idPago>/', login_required(views.eliminar_pago), name='eliminar_pago'),
    path('pagos/editar/<int:id_pago>/', login_required(views.editar_pago), name='editar_pago'),

    ##clientes--------------------------------------

    path('dtclientes/', login_required(views.listado_cliente), name='clientes'),
    path('clientes/', login_required(views.clientes), name='clientes'),
    path('registrarcliente/', login_required(views.registrarcliente), name='registrar_cliente'),
    path('clientes/eliminarcliente/<int:idCliente>/', login_required(views.eliminar_cliente), name='eliminar_cliente'),
    path('clientes/editarcliente/<int:idCliente>/', login_required(views.editar_cliente), name='editar_cliente'),
  
    path('dtclientes/eliminarcliente/<int:idCliente>/', login_required(views.eliminar_cliente), name='eliminar_cliente'),
    path('dtclientes/editarcliente/<int:idCliente>/', login_required(views.editar_cliente), name='editar_cliente'),
 
    ##empleados API--------------------------------------
    
    path('empleados/', EmpleadoListView.as_view(), name='lista-empleados'),  #link del archivo json: http://localhost:8020/empleados/
    path('listar_empleados/', login_required(views.listar_empleados), name='listar_empleados'), #consumo de la api

    ##Detalle venta----------------------------------------
    path('deventa',views.listardeventa,name='listardeventa'),
    path('eliminardeventa/<idDetalle>',views.eliminardeventa),
    path('editardeventa/<idDetalle>',views.editardeventa),
    path('editdeventa',views.editdeventa),
    path('registrardeventa',views.registrardeventa),
    
    path('lista_productos/', login_required(views.reporte_produto.as_view()), name='reporteproductos'),

]
