# -*- coding: utf-8 -*-
import time
import threading
import os
import paho.mqtt.client as paho
import random

ser="115.159.93.53"
isfinished = threading.Event()
isfinished.clear()

mypid = os.getpid()
client = paho.Client("blood_pressure" + str(mypid))
client.connect(ser, port=1883)
uid = 'ID002'
NAME = u'曹操'


try:

    url = 'patients/' + uid
    timestamp = url + '/TS'
    highpressure = url + '/GY'
    lowpressure = url + '/DY'
    maibo = url + '/MB'
    client.publish(url + '/NAME', NAME, 1)

    while client.loop() == 0:

        GY = 100 * random.random()
        DY = 100 * random.random()
        MB = 100 * random.random()

        ts = time.strftime("%Y-%m-%dT%H:%M:%S")

        client.publish(timestamp, ts, 0, 1)
        client.publish(highpressure, GY, 0, 1)
        client.publish(lowpressure, DY, 0, 1)
        client.publish(maibo, MB, 0, 1)
        client.publish(url + '/NAME', NAME, 1)
        print("sent")
        time.sleep(10)

except KeyboardInterrupt:
    print("bye!")
    client.disconnect()
