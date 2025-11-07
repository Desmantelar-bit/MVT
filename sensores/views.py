from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from sensores.models import Sensor, Motor, DadosSensor, SensorMotor
from django.urls import reverse_lazy
from .form import SensorForm, MotorForm, DadosSensorForm, SensorMotorForm

# Create your views here.

class SensorListView(ListView):
    model = Sensor
    template_name = 'sensor_list.html'
    success_url = reverse_lazy('home_list')

class SensorCreateView(CreateView):
    model = Sensor
    form_class = SensorForm
    template_name = 'sensor_form.html'
    success_url = reverse_lazy('sensor_list')

class SensorUpdateView(UpdateView):
    model = Sensor
    form_class = SensorForm
    template_name = 'sensor_form.html'
    success_url = reverse_lazy('sensor_list')

class SensorDeleteView(DeleteView):
    model = Sensor
    template_name = 'sensor_confirm_delete.html'
    success_url = reverse_lazy('sensor_list')

class MotorListView(ListView):
    model = Motor
    template_name = 'motor_list.html'
    sucess_url = reverse_lazy('home_list')

class MotorCreateView(CreateView):
    model = Motor
    form_class = MotorForm
    template_name = 'motor_form.html'
    success_url = reverse_lazy('motor_list')

class MotorUpdateView(UpdateView):
    model = Motor
    form_class = MotorForm
    template_name = 'motor_form.html'
    success_url = reverse_lazy('motor_list')

class MotorDeleteView(DeleteView):
    model = Motor
    template_name = 'motor_confirm_delete.html'
    success_url = reverse_lazy('motor_list')

class DadosSensorListView(ListView):
    model = DadosSensor
    template_name = 'dadossensor_list.html'
    sucess_url = reverse_lazy('home_list')

class DadosSensorCreateView(CreateView):
    model = DadosSensor
    template_name = 'dadossensor_form.html'
    success_url = reverse_lazy('dadossensor_list')

class DadosSensorUpdateView(UpdateView):
    model = DadosSensor
    template_name = 'dadossensor_form.html'
    success_url = reverse_lazy('dadossensor_list')

class DadosSensorDeleteView(DeleteView):
    model = DadosSensor
    template_name = 'dadossensor_confirm_delete.html'
    success_url = reverse_lazy('dadossensor_list')

class SensorMotorListView(ListView):
    model = SensorMotor
    template_name = 'sensormotor_list.html'
    sucess_url = reverse_lazy('home_list')

class SensorMotorCreateView(CreateView):
    model = SensorMotor
    template_name = 'sensormotor_form.html'
    fields = ['MotorId', 'SensorId']
    success_url = reverse_lazy('sensormotor_list')

class SensorMotorUpdateView(UpdateView):
    model = SensorMotor
    template_name = 'sensormotor_form.html'
    success_url = reverse_lazy('sensormotor_list')

class SensorMotorDeleteView(DeleteView):
    model = SensorMotor
    template_name = 'sensormotor_confirm_delete.html'
    success_url = reverse_lazy('sensormotor_list')

class HomeView(ListView):
    model = Motor
    template_name = 'home.html'
