#!/usr/bin/python3

import sys,os,time,csv,getopt,cv2,argparse,ntpath
import numpy as np
from datetime import datetime
#import imutils
import paho.mqtt.client as mqtt

from ObjectWrapper import *
from Visualize import *

#MQTT Client
client=mqtt.Client()
MQTT_SERVER = "192.168.x.xxx"
MQTT_PORT = 1883
MQTT_TOPIC = "home/door/front/camera"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--graph', dest='graph', type=str,
                        default=(os.path.dirname(os.path.realpath(__file__))+'/graph'), help='MVNC graphs.')

    args = parser.parse_args()

    network_blob=args.graph

    #connect to MQTT Server
    client.connect(MQTT_SERVER, MQTT_PORT, 60)
    client.loop_start();

    detector = ObjectWrapper(network_blob)
    stickNum = ObjectWrapper.devNum

    # video preprocess
    cap = cv2.VideoCapture(0)
    #cap = cv2.VideoCapture(videofile)
    fps = 0.0
    while cap.isOpened():
        start = time.time()
        imArr = {}
        results = {}
        for i in range(stickNum):
            ret, img = cap.read()
            img = cv2.flip(img, -1)
            #img = imutils.rotate(img, 180)
            if i not in imArr:
                imArr[i] = img
        if ret == True:
            tmp = detector.Parallel(imArr)
            for i in range(stickNum):
                if i not in results:
                    results[i] = tmp[i]
                mqttframe = Visualize(imArr[i], results[i], fps)
                client.publish(MQTT_TOPIC, mqttframe, 0, False)
            end = time.time()
            seconds = end - start
            fps = stickNum / seconds
            #if cv2.waitKey(1) & 0xFF == ord('q'):
            #    break
