import cv2
import numpy as np

class ObjectTracker(object):
    def __init__(self, scaling_factor=0.5):
        self.cap = cv2.VideoCapture(0)

        #capture the frame from the webcam
        _, self.frame = self.cap.read()

        #scaling factor for the captured frame
        self.scaling_factor = scaling_factor

        # resize the frame
        self.frame = cv2.resize(self.frame, None, fx=self.scaling_factor, fy=self.scaling_factor,interpolation=cv2.INTER_AREA)

        #create a window to display the frame
        cv2.namedWindow('Object Tracker')

        #set the mouse callback function to track the mouse
        cv2.setMouseCallback('Object Tracker', self.mouse_event)

        #Initialize variable related to rectangular selection
        self.selection = None

        #Initialize variable related to starting position
        self.drag_start = None

        #Initialize variable related to the state of tracking
        self.tracking_state = 0

        #Define a method to trace the mouse events

        def mouse_event(self, event, x,y,flags,param):
            #Convert x and y coordinates into 16-bit numpy integers
            x,y = np.int16([x,y])

            # check if a mouse button down event has occurred
            if event == cv2.EVENT_LBUTTONDOWN:
                self.drag_start = (x,y)
                self.tracking_state = 0

            #check if user has started selecting the region
            if self.drag_start:
                if flags & cv2.EVENT_FLAG_LBUTTON:
                    #Extract the dimension of the frame
                    h,w = self.frame.shape[:2]

                    #Get the initial position
                    xi,yi = self.drag_start

                    #Get the max and min volumes
                    x0,y0 = np.maximum(0,np.minimum([xi,yi],[x,y]))
                    x1,y1 = np.minimum([w,h], np.maximum([xi,yi],[x,y]))

                    #Reset the selection variable
                    self.selection = None

                    #Finalize the rectangular selection
                    if x1-x0 >0 and y1-y0>0:
                        self.selection = (x0,y0,x1,y1)

                else:
                    #if selection is done
                    self.drag_start = None
                    if self.selection is not None:
                        self.tracking_state = 1

        #Method to start tracking the object
        def start_tracking(self):
            #Iterate until the user presses the esc key
            while True:

                #Capture the frame from the webcam
                _, self.frame = self.cap.read()



