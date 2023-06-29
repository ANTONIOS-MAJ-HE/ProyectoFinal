from django.db import models

#-----------------TIPO DE PAGO ----------------------------

class Tipopago(models.Model):
    idTipopago = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=255)
    
    def __str__(self):
        return self.tipo
    

#-----------------CATEGORIA ----------------------------
    
class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    

#-----------------CLIENTE ----------------------------

class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    dni = models.IntegerField()
    dirección = models.CharField(max_length=255)
    teléfono = models.IntegerField()
    correo = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    

#-----------------PRODUCTO ----------------------------

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    

#-----------------EMPLEADO ----------------------------
    
class Empleado(models.Model):
    idEmpleado = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    dni = models.IntegerField()
    dirección = models.CharField(max_length=255)
    teléfono = models.IntegerField()
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    

#-----------------PAGO ----------------------------
    
class Pago(models.Model):
    idPago = models.AutoField(primary_key=True)
    numero_tarjeta = models.IntegerField()
    fecha_vencimiento = models.DateField()
    idTipo = models.ForeignKey(Tipopago, on_delete=models.CASCADE)
    cvc = models.IntegerField()

    def __str__(self):
        return self.numero_tarjeta
    

#-----------------VENTA ----------------------------

class Venta(models.Model):
    idVenta = models.AutoField(primary_key=True)
    fecha = models.DateField()
    idcliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idempleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    igv = models.DecimalField(max_digits=10, decimal_places=2)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venta #{self.idVenta}"
    
    
#-----------------DETALLE DE VENTA ----------------------------
    
class Detalleventa(models.Model):
    idDetalle = models.AutoField(primary_key=True)
    idVenta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    montoTotal = models.FloatField()

    def __str__(self):
        return f"Detalle #{self.idDetalle}"
