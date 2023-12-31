

import random

#sql imports
from mysql_connector import db,cursor

#mqtt imports
from paho.mqtt import client as mqtt_client


broker = 'localhost'
port = 1883
print('\n\n')
topic = input("Enter the topic : ")
#"test/client_b"
print('\n')
# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        try:
            message = msg.payload.decode("utf-8")
            topic = msg.topic
            
            querry = f"INSERT IGNORE INTO pub_sub_msg (topic,message)  values (%s,%s)"
            cursor.execute(querry,[topic,message])
            db.commit()
         
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        except Exception as e:
            print(f" Error : {str(e)}")
        

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
    db.close()


if __name__ == '__main__':
    run()
