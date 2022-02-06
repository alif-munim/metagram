import cv2
import mediapipe as mp
import time
import math
import pyautogui

pyautogui.FAILSAFE = False


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionCon, self.trackCon)

        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLm in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLm, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        xList = []
        yList = []
        bbox = []
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                xList.append(cx)
                yList.append(cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)

            bbox = xmin, ymin, xmax, ymax
        return lmList, bbox

    def motionDetector(self, ind, mid, distance=5):
        if not ind or not mid:
            return
        # index finger points
        x1, y1 = ind[1], ind[2]

        # thumb finger points
        x2, y2 = mid[1], mid[2]

        x0, y0 = pyautogui.position()
        # pyautogui.move(x0, y0)
        print(x0, y0)
        length = math.hypot(x2 - x1, y2 - y1)
        if length < distance:
            pyautogui.mouseDown()
            print("click")
        else:
            pyautogui.mouseUp()


def main():
    pTime = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        # print(lmList)

        # print(lmList)
        if len(lmList[0]) != 0:
            detector.motionDetector(lmList[0][8], lmList[0][4], 50)
            # print(lmList[0][4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 9, 255), 3)

        cv2.imshow('Image', img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
