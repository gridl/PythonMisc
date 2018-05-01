import cv2
print("OpenCV version:")
print(cv2.__version__)

# Compute frame differences

def frame_diff(prev_frame, cur_frame, next_frame):
    # Difference between the current frame and the next frame
    diff_frames_1 = cv2.absdiff(next_frame, cur_frame)


    #Difference between the current frame and previous frame
    diff_frames_2 = cv2.absdiff(cur_frame, prev_frame)

    return cv2.bitwise_and(diff_frames_1,diff_frames_2)


# Define a function to get the current frame from the webcam

def get_frame(cap, scaling_factor):
    # Read the current frame from the video capture object
    _, frame = cap.read()


    # resize the image
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

    # Convert o grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    return gray

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

