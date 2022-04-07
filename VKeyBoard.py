from time import sleep
import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector

# Camera

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)


# Draw Button

def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x + 15, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    return img


class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.text = text
        self.pos = pos
        self.size = size


keyList = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
           ["A", "S", "D", "F", "G", "H", "J", "K", "L", ":"],
           ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]

buttonList = []

for i in range(len(keyList)):
    for j, key in enumerate(keyList[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

while True:
    success, img = cap.read()
    # img = detector.findHands(img)
    # lmList = detector.findHands()
    hands, img = detector.findHands(img)
    img = drawAll(img, buttonList)
    if hands:
        # landmarkList
        lmList = hands[0]['lmList']
        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                cv2.rectangle(img, button.pos, (x + w, y + h), (175, 0, 175), cv2.FILLED)
                cv2.putText(img, button.text, (x + 15, y + 65),
                            cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                l, _, _ = detector.findDistance(lmList[8][0:2], lmList[12][0:2], img)
                print(l)
                if l < 45:
                    cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 15, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                    sleep(0.15)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
