from django.db import models

# Create your models here.
class Motor(models.Model):
    Id = models.CharField(primary_key=True, max_length=10)
    Marca = models.CharField(max_length=30)
    Modelo = models.CharField(max_length=30)
    Potencia = models.IntegerField()
    Descricao = models.CharField(max_length=300)
    
    def __str__(self):
        return self.Descricao

class Sensor(models.Model):
    Id = models.CharField(primary_key=True, max_length=10)
    Nome = models.CharField(max_length=30)
    Tipo = models.CharField(max_length=20)
    def __str__(self):
        return self.Nome

class SensorMotor(models.Model):
    MotorId = models.ForeignKey(Motor, on_delete=models.DO_NOTHING )
    SensorId = models.ForeignKey(Sensor, on_delete=models.DO_NOTHING)

class DadosSensor(models.Model):
    id = models.AutoField(primary_key=True)
    DataHora = models.DateTimeField(auto_now=True)
    MotorId = models.ForeignKey(Motor, on_delete=models.DO_NOTHING )
    SensorId = models.ForeignKey(Sensor, on_delete=models.DO_NOTHING)
    Valor = models.FloatField()