#!/usr/bin/python3


# import modules
import cv2
import numpy as np 
from math import sqrt


# Capture mouse position
ix,iy=-1,-1

# True if mouse is pressed
drawing = False

# True for rectangle
# False for circle
mode = True 




# function to draw shape
def draw_shape(event , x,y,flags,param):

    global ix , iy , drawing , mode


    # check if mouse is pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        # change into drawing mode
        drawing=True 
        # capture initial mouse position
        ix,iy=x,y

    # check if mouse is moving
    elif event == cv2.EVENT_MOUSEMOVE:
        # if mouse is pressed  than True
        if drawing:
            #  Draw rectangle
            if mode:
                cv2.rectangle(img , (ix,iy),(x,y),(255,0,0),-1)
            # Draw circle
            else:
                cv2.circle(img,(ix,iy),int(sqrt((x-ix)**2 + (y-iy)**2)),(0,255,0),-1)

    # check if mouse is release            
    elif event == cv2.EVENT_LBUTTONUP:
        # change drawing mode into False
        drawing=False
        # draw rectangle
        if mode:
                cv2.rectangle(img , (ix,iy),(x,y),(255,0,0),-1)
        # Draw circle
        else:
            cv2.circle(img,(x,y),10,(0,255,0),-1)
                    


# create black image of size 512 ,512
img = np.zeros((512,512,3),np.uint8)

# Create window
cv2.namedWindow('image')

# Bind nouse callback function to that window
cv2.setMouseCallback('image',draw_shape)


while True:
    # show image
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF

    # Toggle between Rectangle and Circle
    if k == ord('m'):
        mode = not mode
    #save and break if 'q' is pressed 
    elif k == ord('q'):
        cv2.imwrite('paint_cv.png',img)
        break


# Destroy all created window
cv2.destroyAllWindows()