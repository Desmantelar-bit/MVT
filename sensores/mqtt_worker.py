import os
import sys
import django
import json
import paho.mqtt.client as mqtt
import ssl

# Adiciona o diretório do projeto ao caminho Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)).replace('\\sensores', ''))

# Definição do ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from sensores.models import DadosSensor, Motor, Sensor

# Dados da conexão MQTT
BROKER = "leopard.lmq.cloudamqp.com"  # Host do broker
PORT = 1883  # Porta MQTT padrão sem TLS (use 1883 para conexão não segura)
TOPICO = "dadosSensor"  # Tópico a ser assinado
USERNAME = "idoufayf:idoufayf"  # Usuário do broker
PASSWORD = "DpH2tqSXK2l4s3tx5DNr3_ppS9aYGTis"  # Senha do broker

# Callback para conexão
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("[CONEXÃO] Conectado ao broker MQTT com sucesso!")
        client.subscribe(TOPICO)
        print(f"[CONEXÃO] Inscrito no tópico: {TOPICO}")
    else:
        print(f"[ERRO CONEXÃO] Falha na conexão, RC={rc}")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print(f"[DESCONEXÃO INESPERADA] RC={rc}")
    else:
        print("[DESCONEXÃO] Desconectado do broker")

def on_subscribe(client, userdata, mid, granted_qos):
    print(f"[SUBSCRIÇÃO] Subscrição confirmada com QoS: {granted_qos}")

# Callback para mensagem recebida
def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode('utf-8')
        print(f"[DEBUG] Payload recebido: {payload}")
        dados = json.loads(payload)
        print(f"[DEBUG] JSON parseado: {dados}")
        
        # Extração dos campos do JSON (case-insensitive)
        dados_norm = {k.lower(): v for k, v in dados.items()}

        motor_id = dados.get('MotorId') or dados.get('motorid') or dados_norm.get('motorid')
        sensor_id = dados.get('SensorId') or dados.get('sensorid') or dados_norm.get('sensorid')
        valor_raw = dados.get('Valor') or dados.get('valor') or dados_norm.get('valor')

        missing = []
        if motor_id is None:
            missing.append('MotorId')
        if sensor_id is None:
            missing.append('SensorId')
        if valor_raw is None:
            missing.append('Valor')
        if missing:
            print(f"[ERRO] Campo ausente no JSON: {missing}")
            return

        # normaliza IDs para string (os campos Id são CharField)
        try:
            motor_id = str(motor_id)
            sensor_id = str(sensor_id)
        except Exception as e:
            print(f"[ERRO] Não foi possível converter IDs para string: {e}")
            return

        # Converte valor para float
        try:
            valor = float(valor_raw)
        except Exception as e:
            print(f"[ERRO] Valor numérico inválido: {e}")
            return

        print(f"[DEBUG] Valores extraídos - Motor: {motor_id}, Sensor: {sensor_id}, Valor: {valor}")
        
        # Busca dos objetos relacionados (se não existirem, cria placeholders)
        try:
            motor = Motor.objects.get(Id=motor_id)
            print(f"[DEBUG] Motor encontrado: {motor}")
        except Motor.DoesNotExist:
            print(f"[AVISO] Motor com ID '{motor_id}' não encontrado. Criando registro automático.")
            try:
                motor = Motor.objects.create(Id=motor_id, Marca='Auto', Modelo='Auto', Potencia=0, Descricao='Criado automaticamente pelo worker')
                print(f"[DEBUG] Motor criado: {motor}")
            except Exception as e:
                print(f"[ERRO] Falha ao criar Motor automático: {e}")
                return

        try:
            sensor = Sensor.objects.get(Id=sensor_id)
            print(f"[DEBUG] Sensor encontrado: {sensor}")
        except Sensor.DoesNotExist:
            print(f"[AVISO] Sensor com ID '{sensor_id}' não encontrado. Criando registro automático.")
            try:
                sensor = Sensor.objects.create(Id=sensor_id, Nome='Auto', Tipo='Auto')
                print(f"[DEBUG] Sensor criado: {sensor}")
            except Exception as e:
                print(f"[ERRO] Falha ao criar Sensor automático: {e}")
                return
        
        # Criação e salvamento do registro
        novo_dado = DadosSensor(
            MotorId=motor,
            SensorId=sensor,
            Valor=valor
        )
        novo_dado.save()
        print(f"[SUCESSO] Dado salvo com ID {novo_dado.id}: Motor {motor_id}, Sensor {sensor_id}, Valor {valor}")
    except json.JSONDecodeError as e:
        print(f"[ERRO] JSON inválido: {e}")
    except KeyError as e:
        print(f"[ERRO] Campo ausente no JSON: {e}")
    except ValueError as e:
        print(f"[ERRO] Valor numérico inválido: {e}")
    except Exception as e:
        print(f"[ERRO] Erro ao processar mensagem: {e}")

# Instanciando e configurando o cliente MQTT
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)
client.username_pw_set(USERNAME, PASSWORD)  # Define usuário e senha no cliente MQTT

# Configurar TLS/SSL somente quando porta indicar TLS (ex.: 8883)
if PORT == 8883:
    try:
        client.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_NONE, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
        client.tls_insecure_set(True)
        print("[CONFIG] TLS habilitado (porta 8883)")
    except Exception as e:
        print(f"[AVISO] Não foi possível configurar TLS: {e}")
else:
    # Porta típica sem TLS - 1883
    print("[CONFIG] TLS não habilitado (porta 1883 detectada)")

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.on_subscribe = on_subscribe

print("[INICIALIZAÇÃO] Conectando ao broker MQTT...")
print(f"[CONFIG] Broker: {BROKER}:{PORT}")
print(f"[CONFIG] Usuário: {USERNAME}")
print(f"[CONFIG] Tópico: {TOPICO}")

try:
    client.connect(BROKER, PORT, 60)
    print("[INICIALIZAÇÃO] Conexão iniciada")
    
    print("\n[MQTT WORKER] Iniciando loop MQTT...")
    print("[MQTT WORKER] Aguardando mensagens (pressione CTRL+C para parar)...\n")
    
    # Usar loop_start() para não bloquear
    client.loop_start()
    
    # Manter o script rodando
    import time
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[MQTT WORKER] Encerrando...")
        client.loop_stop()
        client.disconnect()
        
except Exception as e:
    print(f"[ERRO CONEXÃO] Falha ao conectar: {e}")
    exit(1)
