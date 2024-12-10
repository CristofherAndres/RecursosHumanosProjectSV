from rest_framework import serializers
from EmpleadosApp.models import Empleado

class EmpleadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'