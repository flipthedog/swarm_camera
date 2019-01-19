# Taking a picture
import cv2 as cv

capture = cv.VideoCapture(0)
print("Taking pic")
ret, frame = capture.read()

cv.imshow('Your Picture', frame)

while True:
    if cv.waitKey(1) & 0xFF == ord('y'):
        cv.imwrite('hackathon_1.png',frame)
        print("Waiting")
        cv.destroyAllWindows()
        break

capture.release()