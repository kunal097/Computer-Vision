#!/usr/bin/python3


# import cv2 module
import cv2

# import numpy for image manupulation
import numpy as np


# Create white image of size 512,512,3
img = np.full((512, 512, 3), 255, np.uint8)


# Create ellipse of equal axis
cv2.ellipse(img, (225, 185), (40, 40), 0, 400, 140, (0, 0, 255), 30)
cv2.ellipse(img, (170, 280), (40, 40), 220, 400, 140, (0, 255, 0), 30)
cv2.ellipse(img, (290, 280), (40, 40), 180, 400, 140, (255, 0, 0), 30)


# Specify font family
font = cv2.FONT_HERSHEY_COMPLEX


# Write text
cv2.putText(img, 'Open CV', (100, 450), font,
            2, (150, 10, 50), 2, cv2.LINE_4)


# Display created image
cv2.imshow('white', img)


# Save image
cv2.imwrite('cv_icon.png', img)


# Wait infinetly
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
