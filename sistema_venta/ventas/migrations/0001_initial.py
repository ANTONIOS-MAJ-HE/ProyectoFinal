# Generated by Django 4.2.2 on 2023-06-29 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idCliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255)),
                ('dni', models.IntegerField()),
                ('dirección', models.CharField(max_length=255)),
                ('teléfono', models.IntegerField()),
                ('correo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('idEmpleado', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255)),
                ('dni', models.IntegerField()),
                ('dirección', models.CharField(max_length=255)),
                ('teléfono', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Tipopago',
            fields=[
                ('idTipopago', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('idVenta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('igv', models.DecimalField(decimal_places=2, max_digits=10)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('idcliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.cliente')),
                ('idempleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('idCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('idPago', models.AutoField(primary_key=True, serialize=False)),
                ('numero_tarjeta', models.IntegerField()),
                ('fecha_vencimiento', models.DateField()),
                ('cvc', models.IntegerField()),
                ('idTipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.tipopago')),
            ],
        ),
        migrations.CreateModel(
            name='Detalleventa',
            fields=[
                ('idDetalle', models.AutoField(primary_key=True, serialize=False)),
                ('precio', models.FloatField()),
                ('cantidad', models.IntegerField()),
                ('montoTotal', models.FloatField()),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.producto')),
                ('idVenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.venta')),
            ],
        ),
    ]
