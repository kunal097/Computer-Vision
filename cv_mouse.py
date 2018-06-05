#!/usr/bin/python3

# import modules

import cv2
import numpy as np 




# Draw circle of different color on behalf of EVENTS

def draw_circle(event , x,y,flags,param):	

	# if Left mouse click then draw Blue circle
	if event == cv2.EVENT_LBUTTONDOWN:	
		cv2.circle(img,(x,y),100,(255,0,0),-1)


	# if Middle mouse click then draw Green circle  
	if event == cv2.EVENT_MBUTTONDOWN:
		cv2.circle(img,(x,y),100,(0,255,0),-1)

	# if Right mouse click then draw Red circle
	if event == cv2.EVENT_RBUTTONDOWN:
		cv2.circle(img,(x,y),100,(0,0,255),-1)		




# create black image
img = np.zeros((512,512,3),np.uint8)

# create window
cv2.namedWindow('image')
#Bind mouse event tracker on that window
cv2.setMouseCallback('image' , draw_circle)




while True:
	# Show image
	cv2.imshow('image',img)

	# Break when q is pressed
	if cv2.waitKey(1) & 0xFF == ord('q'):
		cv2.imwrite('cv_mouse.png',img)
		break


# Destroy all created windows
cv2.destroyAllWindows()		

