"""
URL configuration for RecursosHumanosProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from EmpleadosApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empleado/', Empleado),
    path('empleadoV2/', EmpleadoV2),
    path('empleadosAPI/', Empleado_List),
    path('empleadosAPI/<int:pk>', Empleado_Detail),
    path('cEmpleadoAPI/', EmpleadoList.as_view()),
    path('cEmpleadoAPI/<int:pk>', EmpleadoDetail.as_view())
]
