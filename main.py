import cv2

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()

    if _ is not None:
        img = cv2.flip(img, 1)
        cv2.imshow("Image", img)
    
    if cv2.waitKey(1) == 27:
        break