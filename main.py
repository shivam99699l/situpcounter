import cv2
from cvzone.PoseModule import PoseDetector
import numpy as np

per = 0
cap = cv2.VideoCapture(0)
detector = PoseDetector()
angle = 0
color = (0, 0, 225)
situps = 0
dir = 0
while True:
    _, img = cap.read()
    img = detector.findPose(img)  # add false argument to hide lines.
    lmlist, bbox = detector.findPosition(img, False)

    if lmlist:
        # print(lmlist)
        angle = detector.findAngle(img, 24, 26, 28)
        per = np.interp(angle, (40, 165), (100, 0))
        bar_value = np.interp(angle, (40, 165), (15, 15 + 300))

        cv2.rectangle(img, (500, int(bar_value)), (500 + 30, 15 + 300), color, cv2.FILLED)
        cv2.rectangle(img, (500, 15), (500 + 30, 15 + 300), (), 3)

        cvzone.putTextRect(img, f'{int(per)} %', (575, 350), 1.2, 2, colorT=(), colorR=color, border=3, colorB=())

        if per == 100:
            if dir == 0:
                situps += 0.5
                dir = 1
        elif per == 0:
            if dir == 1:
                situps += 0.5
                dir = 0
        print(situps)
        cvzone.putTextRect(img, str(int(situps)), (40, 40), 2, 2)
    cv2.imshow('situps counter', img)
    if cv2.waitKey(1) == ord('a'):
        break

