from django.urls import path
from . import views

urlpatterns = [

    path('', views.homes, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),

    ##Producto-----------------------------------------
    path('dataproducto/',views.listarproductos,name='listarproductos'),
    ##path('producto/',views.buscarproductos,name='home'),
    path('registrarproducto',views.registrarproductos,name='registrarproducto'),
    path('productos', views.productos, name='productos'),
    path('editarproducto/<str:idProducto>/', views.editarproductos, name='editarproducto'),
]