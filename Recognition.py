import cv2
import numpy as np
import os
import time
import datetime

confidence_threshold = 90

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

id = 0

names = ['None', 'Person 1', 'Person 2']

cam = cv2.VideoCapture(0)
cam.set(3, 640) 
cam.set(4, 480)

# Define min window size to be recognized as a face
minW = 0.05*cam.get(3)
minH = 0.05*cam.get(4)

flag_person = 0

while True:

    now = datetime.datetime.now()
    t = now.hour
    if (t>6 and t<12):
        ret, img =cam.read()
        
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )

        for(x,y,w,h) in faces:

            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            if (confidence < confidence_threshold):
                id = names[id]
                print(id,' spotted at ',now.hour,':',now.minute,'on',now.month,'/',now.day)
                confidence = "  {0}%".format(round(100 - confidence))
                if (id == 'Person1' and flag_person_ == 0):
                    os.system('message')
                    time.sleep(5)
                    os.system('message')
                    time.sleep(10)
                    os.system('mycroft-speak have a great day ahead')
                    flag_person_ = 1
                time.sleep(60)

            else:
                    id = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))
    elif (t>14):

        ret, img =cam.read()

        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )

        for(x,y,w,h) in faces:

            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

            if (confidence < confidence_threshold):
                id = names[id]
                print(id,' spotted at ',now.hour,':',now.minute,'on',now.month,'/',now.day)
                confidence = "  {0}%".format(round(100 - confidence))
                if (id == 'person' and flag_person == 0):
                    os.system('mycroft-speak welcome home person, I hope you had a wondeful day')
                    flag_person_ = 1
                time.sleep(60)

            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))

    else:
        time.sleep(120)
        flag_person_ = 0

