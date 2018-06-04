#!/usr/bin/python3


# import cv2 module
import cv2


# Specify choices
choice = '''

	Press -->
	1. Default camera
	2. Test Video (Default case)

'''

# get user choice
ch = int(input(choice))


if ch == 1:
    # create VideoCapture object (0 -> default camera)
    cap = cv2.VideoCapture(0)
else:
    # create VideoCapture object
    cap = cv2.VideoCapture('nature.mp4')


# define video codec/format
fourcc = cv2.VideoWriter_fourcc(*'XVID')


# get window size
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


# Create videoWriter object
#Arguments  (file-name , fourcc , Number_of_frame , window_size)
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (width, height))


# loop until 'q' is  pressed
while True:

    # check if cap is initialised or not .
    if cap.isOpened():

        # read from camera , return status(True/False) and frame (Video frame)
        status, frame = cap.read()

        # flip the frame window
        gray = cv2.flip(frame, 0)

        # write to the VideoWriter object
        out.write(gray)

        # Show Video frame
        cv2.imshow('CV video', frame)

        # exit when 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


# Release previously initiated object
cap.release()
out.release()

# Destroy all Windows
cv2.destroyAllWindows()
