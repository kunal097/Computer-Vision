#!/usr/bin/python3


# import cv2 module
import cv2

# import numpy for doing manupulation in images
import numpy as np


# create black image of size 512,512
img = np.zeros((512, 512, 3), dtype='uint8')


# Draw line
# cv2.line(image,starting_point , end_point,(B,G,R),width)
cv2.line(img, (0, 0), (512, 512), (0, 255, 0), 3)


# Draw rectangle
# cv2.rectangle(image , top_left_point , bottom_right_point , (B,G,R),width)
cv2.rectangle(img, (256, 10), (510, 256), (255, 0, 0), 3)


# Draw circle
# cv2.circle(image,center,radius,(B,G,R),width)
cv2.circle(img, (383, 143), 50, (0, 0, 255), -1)


# Draw ellipse
# cv2.ellipse(image,center,(length_of_major_axis , length_of_minor_axis),angle_of_rotation,start_angle,end_angle,(B,G,R),width)
cv2.ellipse(img, (156, 356), (100, 50), 90, 0, 360, (156, 100, 200), -1)


# create array of different points
pts = np.array([[10, 10], [20, 50], [70, 30], [60, 50], [10, 70]], np.int32)
# reshape into rows,1,2 (x=no. of points)
pts = pts.reshape((-1, 1, 2))

# Create polygon
# cv2.polylines(image , [array_of_points],bool,(B,G,R))
# True --> closed shape
# False --> join all points but not closed
cv2.polylines(img, [pts], True, (100, 100, 200))


# Create multiple lines using cv2.polylines()
pts1 = np.array([[10, 100], [50, 200]], np.int32).reshape((-1, 1, 2))
pts2 = np.array([[10, 200], [50, 300]], np.int32).reshape((-1, 1, 2))
cv2.polylines(img, [pts1, pts2], True, (250, 100, 200))


# Write text on image
# Specify font
font = cv2.FONT_HERSHEY_SIMPLEX

# Write text
# cv2.putText(image,text,coordinate,font_family,font_size,(B,G,R),width,line_type)
cv2.putText(img, 'CV is fun', (100, 500), font,
            2, (250, 250, 250), 2, cv2.LINE_AA)


# Show image after drawing all the above shape
cv2.imshow('window', img)

# save all the changes
cv2.imwrite('cv_shapes.png', img)

# wait till key is pressed
cv2.waitKey(0)

# destroy all windows
cv2.destroyAllWindows()
