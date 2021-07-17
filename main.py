import cv2
from HandDetectorModule.tracker import HandDetector
from math import sqrt

cap = cv2.VideoCapture(0)

# Initialize hand detector object
detector = HandDetector(maxHands=1,
                        min_detect_conf=0.65,
                        min_track_conf=0.7)

# Initialize the landmarks list to calculate the distance between
# THUMB_TIP and INDEX_FINGER_TIP to control volume
landmarks = []

while True:
    _, img = cap.read()

    if _ is not None:
        img = cv2.flip(img, 1)
        img = detector.findHands(img)

        landmarks = detector.findPosition(img, handNo=0, landmarks=[4, 8])

        if len(landmarks) > 1:
            x1, y1 = landmarks[0]
            x2, y2 = landmarks[1]

            distance = sqrt((x2-x1)**2 + (y2-y1)**2)

            cv2.putText(img, str(distance), (20, 70),
                        cv2.FONT_HERSHEY_DUPLEX, 1,
                        (0, 255, 0), 2)

        cv2.imshow("Image", img)

    if cv2.waitKey(1) == 27:
        break
