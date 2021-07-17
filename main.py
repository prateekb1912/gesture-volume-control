import cv2
from HandDetectorModule.tracker import HandDetector

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

        cv2.imshow("Image", img)

    if cv2.waitKey(1) == 27:
        break
