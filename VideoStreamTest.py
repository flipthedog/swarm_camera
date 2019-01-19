import cv2 as cv
from swarm_camera.ImageProcessing import process_image as process

cap = cv.VideoCapture(0)
while 1:


    ret, frame = cap.read()

    gray = process.grayImage(frame)
    thresh = process.thresholdImage(gray, 1, 1)
    eroded = process.morphTrans(thresh, 1, 2, 1)
    contour = process.contourImage(gray)
    edge = process.edgeDetection(gray)
    inv = process.invertImage(edge)

    cv.imshow("Live", contour)
    if cv.waitKey(1) & 0xFF == ord('y'):
        print("Exiting")
        cv.destroyAllWindows()
        break