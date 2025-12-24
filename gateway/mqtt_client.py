import paho.mqtt.client as mqtt

def connect_mqtt(broker="test.mosquitto.org", port=1883):
    client = mqtt.Client()
    client.connect(broker, port)
    return client
