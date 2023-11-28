# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 19:14:02 2022

@author: Justice Nyarko
"""

import cv2
 
#img = cv2.imread("justice.jpg") 

cap = cv2.VideoCapture('youtube.mp4')
cap.set(3, 640)
cap.set(4,480)

classNames =[]
classFiles = 'coco.names'

with open(classFiles,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')


configPath = 'ssd_mobilenet_V3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)


while True:
    success, img = cap.read()
    classIds, confs, bbox = net.detect(img, confThreshold = 0.5)
    print(classIds, bbox)
    
    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(),confs.flatten(),bbox):
            cv2.rectangle(img, box,color=(0, 255, 0),thickness = 3)
            cv2.putText(img, classNames[classId-1].upper(),(box[0]+10, box[1]+30),
                        cv2.FONT_HERSHEY_COMPLEX,1,(0, 255,0),2)
    
    cv2.imshow("Output", img)
    cv2.waitKey(1)