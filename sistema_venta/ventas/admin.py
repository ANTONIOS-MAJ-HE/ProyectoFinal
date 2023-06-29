from django.contrib import admin
from .models import Producto, Tipopago, Categoria, Cliente, Empleado, Pago, Venta, Detalleventa
# Register your models here.

admin.site.register(Producto)
admin.site.register(Tipopago)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Pago)
admin.site.register(Venta)
admin.site.register(Detalleventa)