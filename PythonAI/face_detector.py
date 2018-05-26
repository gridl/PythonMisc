import cv2
import numpy as np

# load the HAAR cascade file
face_cascade = cv2.CascadeClassifier('frontalFace10/haarcascade_frontalface_default.xml')


if face_cascade.empty():
    raise IOError("Unable to load the face cascade classfier xml file")


# initialize the video capture object

cap = cv2.VideoCapture(0)

# Define the scaling factor
scaling_factor = 0.5

# Iterate until the user hits the 'esc' key
while True:
    #Capture the current frame
    _, frame = cap.read()

    #resize the frame
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

    #convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Run the face detector on the grayscale image
    face_rects = face_cascade.detectMultiScale(gray,1.3,5)

    #Draw a rectangle around the face
    for (x,y,w,h) in face_rects:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    #dispaly the output
    cv2.imshow('Face Detector', frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()

cv2.destroyAllWindows()