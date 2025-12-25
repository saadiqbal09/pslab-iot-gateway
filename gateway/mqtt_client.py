import paho.mqtt.client as mqtt
import time
from paho.mqtt.enums import CallbackAPIVersion


def publish_test():
    client = mqtt.Client(CallbackAPIVersion.VERSION2)
    client.connect("test.mosquitto.org", 1883, 60)

    for i in range(5):
        msg = f"test_value_{i}"
        client.publish("pslab/test", msg)
        print("Published:", msg)
        time.sleep(1)

    client.disconnect()

if __name__ == "__main__":
    publish_test()

