from django.shortcuts import render
from django.http import JsonResponse

##IMPORTACIONES PARA API
from EmpleadosApp.models import Empleado
from EmpleadosApp.serializers import EmpleadoSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# API CLASE
from rest_framework.views import APIView

# Create your views here.
def EmpleadoV1(request):
    empleado = {
        'id':1,
        'nombre':'Juan',
        'apellido':'Perez',
        'edad':30,
        'salario':50000
    }
    return JsonResponse(empleado)

def EmpleadoV2(request):
    empleados = Empleado.objects.all()
    data = {'empleados' : list(empleados.values('nombre','apellido'))}
    return JsonResponse(data)

# GET /EmpleadosAPi -> Listar todos los empleados
# POST /EmpleadosApi -> Crear un empleado

@api_view(['GET','POST'])
def Empleado_List(request):
    if request.method == 'GET':
        empleados = Empleado.objects.all() #SELECT * FROM Empleado
        serializer = EmpleadoSerializers(empleados, many=True) #Convertir a JSON
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = EmpleadoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
# GET /EmpleadosAPi/1 -> Obtener un empleado
# PUT /EmpleadosApi/1 -> Actualizar un empleado
# DELETE /EmpleadosApi/1 -> Borrar un empleado

@api_view(['GET','PUT','DELETE'])
def Empleado_Detail(request, pk):
    try:
        empleado = Empleado.objects.get(pk=pk)
    except Empleado.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EmpleadoSerializers(empleado)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = EmpleadoSerializers(empleado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        empleado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# API CON CLASE

class EmpleadoList(APIView):
    
    def get(self, request):
        empleados = Empleado.objects.all() #SELECT * FROM Empleado
        serializer = EmpleadoSerializers(empleados, many=True) #Convertir a JSON
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EmpleadoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EmpleadoDetail(APIView):
    def get_object(self, request, pk):
        try:
            empleado = Empleado.objects.get(pk=pk)
        except Empleado.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        empleado = Empleado.objects.get(pk=pk)
        serializer = EmpleadoSerializers(empleado)
        return Response(serializer.data)

    def put(self, request, pk):
        empleado = Empleado.objects.get(pk=pk)
        serializer = EmpleadoSerializers(empleado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        empleado = Empleado.objects.get(pk=pk)
        empleado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)