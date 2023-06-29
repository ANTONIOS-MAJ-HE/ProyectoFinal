from django.urls import path
from . import views


app_name = 'ventas'
urlpatterns = [

    path('', views.homes, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('dtventas/', views.listadoventa, name='dtventas'),
    path('registrarventa/', views.registrarventa, name='registrarventa'),
    path('dtventas/eliminarventa/<idVenta>', views.eliminarventa),
    path('dtventas/editarventa/<int:id_venta>', views.editar_venta, name='editar_venta'),
]