# -*- coding: utf-8 -*-

import redis
import os
import json
import paho.mqtt.client as paho
ser="115.159.93.53"
mypid = os.getpid()
client = paho.Client("blood_pressure_rec"+str(mypid), clean_session=False)
conn = redis.Redis('localhost')


def SendToRedisHash(uid, tagvaluedict):

    pipe = conn.pipeline()
    for key in tagvaluedict:
        pipe.hmset('%s.%s' % (uid, key), tagvaluedict[key])

    pipe.execute()


def on_message(mosq, obj, msg):
    # called when we get an MQTT message that we subscribe to
    slist = msg.topic.split("/")
    try:
        #dic1 = json.loads(msg.payload.decode())
        #SendToRedisHash(slist[1], dic1)

        value=msg.payload.decode()
        print(slist)
        conn.set('%s.%s' % (slist[1], slist[2]), value)
        print(slist[1])
    except Exception:
        print("Illegal Data: %s" % msg.payload.decode())


def connectall():
    print("DISPATCHER: Connecting")
    client.connect(host=ser, port=1883)
    print('Connected')
    client.subscribe("patients/#", 1)
    client.on_message = on_message


def disconnectall():
    print("DISPATCHER: Disconnecting")
    client.disconnect()


if __name__ == '__main__':
    connectall()
    try:
        while client.loop() == 0:
            pass
        # Look for commands in the queue and execute them

    except KeyboardInterrupt:
        print("Interrupt received")
        disconnectall()
