import cv2
import numpy as np

# define function to get current frame
def get_frame(cap, scaling_factor):
    _, frame = cap.read()


    # resize image
    frame = cv2.resize(frame,None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    return frame


if __name__ == '__main__':
    # define the video capture object
    cap = cv2.VideoCapture(0)


    # Define background subtractor object
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()

    history = 100

    learning_rate = 1.0/history

    while True:

        frame = get_frame(cap, 0.5)

        # compute the mask
        mask = bg_subtractor.apply(frame, learningRate=learning_rate)

        # convert grayscale image to RGB color image
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

        # display the images

        cv2.imshow('Input', frame)
        cv2.imshow('Output', mask & frame)

        c = cv2.waitKey(10)
        if c == 27:
            break

cap.release()

cv2.destroyAllWindows()

