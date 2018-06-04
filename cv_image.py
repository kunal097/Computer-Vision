#!/usr/bin/python3

import cv2


# read image in grayscale mode

img = cv2.imread('d1.jpg',0)


# create window
cv2.namedWindow('Open cv Image')


# Show image in the above window
cv2.imshow('Open cv Image',img)


# Wait unitl key is pressed and record keystoke
k = cv2.waitKey(0) & 0xFF


if k==27:  # Esc is pressed exit without saving
	# Destroy all windows
	cv2.destroyAllWindows()

elif k==115: # S  is pressed therefore save and exit
	cv2.imwrite('newImg.png',img)
	cv2.destroyAllWindows()