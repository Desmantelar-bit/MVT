from django import forms
from .models import Sensor, Motor, DadosSensor, SensorMotor

class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['Id','Nome', 'Tipo']
        labels = {
            'Id': 'ID do Sensor',
            'Nome': 'Nome do Sensor',
            'Tipo': 'Tipo de Sensor',
        }

class MotorForm(forms.ModelForm):
    class Meta:
        model = Motor
        fields = ['Id','Marca', 'Modelo', 'Potencia', 'Descricao']
        labels = {
            'Id': 'ID do Motor',
            'Marca': 'Marca do Motor',
            'Modelo': 'Modelo do Motor',
            'Potencia': 'Potência (HP)',
            'Descricao': 'Descrição do Motor',
        }

class SensorMotorForm(forms.ModelForm):
    class Meta:
        model = SensorMotor
        fields = ['MotorId', 'SensorId']
        labels = {
            'MotorId': 'Motor',
            'SensorId': 'Sensor',
        }

class DadosSensorForm(forms.ModelForm):
    class Meta:
        model = DadosSensor
        fields = ['id','MotorId','SensorId', 'Valor']
        labels = {

            'id': 'ID do Dado',
            'MotorId': 'Motor',
            'SensorId': 'Sensor',
            'Valor': 'Valor do Sensor',
        }

