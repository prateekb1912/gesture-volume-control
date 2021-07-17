import cv2
from HandDetectorModule.tracker import HandDetector

cap = cv2.VideoCapture(0)

# Initialize hand detector object
detector = HandDetector(maxHands=1,
                        min_detect_conf=0.65,
                        min_track_conf=0.7)
while True:
    _, img = cap.read()

    if _ is not None:
        img = cv2.flip(img, 1)

        cv2.imshow("Image", img)

    if cv2.waitKey(1) == 27:
        break
