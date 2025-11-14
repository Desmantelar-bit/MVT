from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from sensores.models import Sensor, Motor, DadosSensor, SensorMotor
from django.urls import reverse_lazy
from .form import SensorForm, MotorForm, DadosSensorForm, SensorMotorForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse


# Create your views here.
def dashboard(request):
    total_motores = Motor.objects.count()
    total_sensores = Sensor.objects.count()
    total_sensor_motor = SensorMotor.objects.count()
    ultimos_dados = DadosSensor.objects.order_by('-DataHora')[:10]

    context = {
        'total_motores': total_motores,
        'total_sensores': total_sensores,
        'total_sensor_motor': total_sensor_motor,
        'ultimos_dados': ultimos_dados,
    }

    return render(request, 'dashboard.html', context)


def api_ultimos_dados(request):
    """Retorna JSON com os últimos 10 registros de DadosSensor."""
    ultimos = DadosSensor.objects.order_by('-DataHora')[:10]
    data = []
    for d in ultimos:
        data.append({
            'id': d.id,
            'datahora': d.DataHora.strftime('%Y-%m-%d %H:%M:%S'),
            'sensor_id': d.SensorId.Id,
            'sensor_nome': d.SensorId.Nome,
            'motor_id': d.MotorId.Id,
            'motor_marca': d.MotorId.Marca,
            'motor_modelo': d.MotorId.Modelo,
            'valor': d.Valor,
        })
    return JsonResponse({'ultimos_dados': data})

class SensorListView(LoginRequiredMixin, ListView):
    model = Sensor
    template_name = 'sensor_list.html'
    success_url = reverse_lazy('home_list')

class SensorCreateView(LoginRequiredMixin, CreateView):
    model = Sensor
    form_class = SensorForm
    template_name = 'sensor_form.html'
    success_url = reverse_lazy('sensor_list')

class SensorUpdateView(LoginRequiredMixin, UpdateView):
    model = Sensor
    form_class = SensorForm
    template_name = 'sensor_form.html'
    success_url = reverse_lazy('sensor_list')

class SensorDeleteView(LoginRequiredMixin, DeleteView):
    model = Sensor
    template_name = 'sensor_confirm_delete.html'
    success_url = reverse_lazy('sensor_list')

class MotorListView(LoginRequiredMixin, ListView):
    model = Motor
    template_name = 'motor_list.html'
    success_url = reverse_lazy('home_list')

class MotorCreateView(LoginRequiredMixin, CreateView):
    model = Motor
    form_class = MotorForm
    template_name = 'motor_form.html'
    success_url = reverse_lazy('motor_list')

class MotorUpdateView(LoginRequiredMixin, UpdateView):
    model = Motor
    form_class = MotorForm
    template_name = 'motor_form.html'
    success_url = reverse_lazy('motor_list')

class MotorDeleteView(LoginRequiredMixin, DeleteView):
    model = Motor
    template_name = 'motor_confirm_delete.html'
    success_url = reverse_lazy('motor_list')

class DadosSensorListView(LoginRequiredMixin, ListView):
    model = DadosSensor
    template_name = 'dadossensor_list.html'
    sucess_url = reverse_lazy('home_list')

class DadosSensorCreateView(LoginRequiredMixin, CreateView):
    model = DadosSensor
    template_name = 'dadossensor_form.html'
    success_url = reverse_lazy('dadossensor_list')

class DadosSensorUpdateView(LoginRequiredMixin, UpdateView):
    model = DadosSensor
    template_name = 'dadossensor_form.html'
    success_url = reverse_lazy('dadossensor_list')

class DadosSensorDeleteView(LoginRequiredMixin, DeleteView):
    model = DadosSensor
    template_name = 'dadossensor_confirm_delete.html'
    success_url = reverse_lazy('dadossensor_list')

class SensorMotorListView(LoginRequiredMixin, ListView):
    model = SensorMotor
    template_name = 'sensormotor_list.html'
    sucess_url = reverse_lazy('home_list')

class SensorMotorCreateView(LoginRequiredMixin, CreateView):
    model = SensorMotor
    template_name = 'sensormotor_form.html'
    fields = ['MotorId', 'SensorId']
    success_url = reverse_lazy('sensormotor_list')

class SensorMotorUpdateView(LoginRequiredMixin,UpdateView):
    model = SensorMotor
    template_name = 'sensormotor_form.html'
    success_url = reverse_lazy('sensormotor_list')

class SensorMotorDeleteView(LoginRequiredMixin, DeleteView):
    model = SensorMotor
    template_name = 'sensormotor_confirm_delete.html'
    success_url = reverse_lazy('sensormotor_list')

class HomeView(LoginRequiredMixin, ListView):
    model = Motor
    template_name = 'home.html'
