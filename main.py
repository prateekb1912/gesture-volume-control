import cv2
from HandDetectorModule.tracker import HandDetector
from math import hypot
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import numpy as np

cap = cv2.VideoCapture(0)

cv2.namedWindow("Gesture Control", cv2.WINDOW_KEEPRATIO)
# cv2.resizeWindow("Gesture Control", 1280, 640)

# Initialize hand detector object
detector = HandDetector(maxHands=1,
                        min_detect_conf=0.6,
                        min_track_conf=0.7)

# Initialize the landmarks list to calculate the distance between
# THUMB_TIP and INDEX_FINGER_TIP to control volume
landmarks = []
devices = AudioUtilities.GetSpeakers()

interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None
)

volume = cast(interface, POINTER(IAudioEndpointVolume))

volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]

distRange = [25, 250]
volBarZero = (85, 400)
volBarMax = (50, 150)

while True:
    _, img = cap.read()

    if _ is not None:
        img = cv2.flip(img, 1)
        img = detector.findHands(img)

        landmarks = detector.findPosition(img, handNo=0, landmarks=[4, 8])

        if len(landmarks) > 1:
            x1, y1 = landmarks[0]
            x2, y2 = landmarks[1]

            distance = hypot(x2-x1, y2-y1)

            # The range of distance is between 25 & 275
            # The volume range is -65 to 0

            vol = np.interp(distance, distRange, [minVol, maxVol])
            level = np.interp(distance, distRange, [volBarZero[1], volBarMax[1]])
            perc = np.interp(distance, distRange, [0, 100])

            if perc > 80:
                print(vol)
                print(distance)
                print(perc)
            cv2.rectangle(img, volBarZero, (volBarMax[0], int(level)), (0, 0, 255), cv2.FILLED)
            cv2.putText(img, str(int(perc)), (55, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

            volume.SetMasterVolumeLevel(vol, None)

        cv2.rectangle(img, volBarMax, volBarZero, (0, 255, 0), 3)

        cv2.imshow("Gesture Control", img)

        if cv2.waitKey(1) == 27:
            break

cv2.destroyAllWindows()