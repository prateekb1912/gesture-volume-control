import cv2
from HandDetectorModule.tracker import HandDetector
from math import hypot
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import numpy as np

cap = cv2.VideoCapture(0)

# Initialize hand detector object
detector = HandDetector(maxHands=1,
                        min_detect_conf=0.65,
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
volume.SetMasterVolumeLevel(0, None)

minVol = volRange[0]
maxVol = volRange[1]

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

            # The range of distance is between 10 & 300
            # The volume range is -65 to 0

            volumeControl()

        cv2.imshow("Image", img)

        if cv2.waitKey(1) == 27:
            break