"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from sensores.views import SensorListView, SensorCreateView, SensorUpdateView, SensorDeleteView
from sensores.views import MotorListView, MotorCreateView, MotorUpdateView, MotorDeleteView
from sensores.views import DadosSensorListView, DadosSensorCreateView, DadosSensorUpdateView,  DadosSensorDeleteView
from sensores.views import SensorMotorListView, SensorMotorCreateView, SensorMotorUpdateView, SensorMotorDeleteView
from sensores.views import HomeView
from django.urls import include

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    # Sensor URLs
    path('sensors/', SensorListView.as_view(), name='sensor_list'),
    path('sensors/add/', SensorCreateView.as_view(), name='sensor_form'),
    path('sensors/<int:pk>/edit/', SensorUpdateView.as_view(), name='sensor_form'),
    path('sensors/<int:pk>/delete/', SensorDeleteView.as_view(), name='sensor_delete'),

    # Motor URLs
    path('motors/', MotorListView.as_view(), name='motor_list'),
    path('motors/add/', MotorCreateView.as_view(), name='motor_form'),
    path('motors/<int:pk>/edit/', MotorUpdateView.as_view(), name='motor_form'),
    path('motors/<int:pk>/delete/', MotorDeleteView.as_view(), name='motor_delete'),

    # DadosSensor URLs
    path('dadossensores/', DadosSensorListView.as_view(), name='dadossensor_list'),
    path('dadossensores/add/', DadosSensorCreateView.as_view(), name='dadossensor_form'),
    path('dadossensores/<int:pk>/edit/', DadosSensorUpdateView.as_view(), name='dadossensor_form'),
    path('dadossensores/<int:pk>/delete/', DadosSensorDeleteView.as_view(), name='dadossensor_delete'),
    
    # SensorMotor URLs
    path('sensormotors/', SensorMotorListView.as_view(), name='sensormotor_list'),
    path('sensormotors/add/', SensorMotorCreateView.as_view(), name='sensormotor_form'),
    path('sensormotors/<int:pk>/edit/', SensorMotorUpdateView.as_view(), name='sensormotor_form'),
    path('sensormotors/<int:pk>/delete/', SensorMotorDeleteView.as_view(), name='sensormotor_delete'),
    
    ]
