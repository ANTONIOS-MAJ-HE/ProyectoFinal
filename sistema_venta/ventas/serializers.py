from rest_framework import serializers

from ventas.models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['idEmpleado', 'nombres', 'apellidos', 'dni', 'dirección', 'teléfono', 'correo']
