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

                #resize the input frame
                self.frame = cv2.resize(self.frame, None, fx=self.scaling_factor, fy=self.scaling_factor,interpolation=cv2.INTER_AREA)

                #create a copy of the frame
                vis = self.frame.copy()

                #convert the frame to HSV colorspace
                hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

                #create the mask based on predefined
                mask = cv2.inRange(hsv, np.array(0.,60.,32.)),np.array((180.,255.,255.))

                #check if the user has select the region
                if self.selection:
                    x0,y0,x1,y1 = self.selection
                    self.track_window = (x0,y0,x1-x0,y1-y0)

                    hsv_roi = hsv[y0:y1,x0:x1]
                    mask_roi = mask[y0:y1,x0:x1]

                    hist = cv2.calcHist([hsv_roi],[0],mask_roi,[16],[0,180])

                    cv2.normalize(hist,hist,0,255,cv2.NORM_MINMAX);
                    self.hist = hist.reshape(-1)

                    vis_roi = vis[y0:y1,x0:x1]

                    cv2.bitwise_not(vis_roi,vis_roi)
                    vis[mask ==0] =0

                if self.tracking_state == 1:
                    self.selection = None

                    hsv_backproj = cv2.calcBackProject([hsv],[0], self.hist,[0,180],1)

                    hsv_backproj &= mask

                    term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,1)

                    track_box, self.track_window = cv2.CamShift(hsv_backproj,self.track_window, term_crit)

                    cv2.ellipse(vis,track_box,(0,255,0),2)

                cv2.imshow('Object Tracker', vis)

                c = cv2.waitKey(5)
                if c ==27:
                    break

        cv2.destroyAllWindows()

if __name__ == '__main__':
    ObjectTracker().start_tracking()











