import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)
img = cv2.imread("Lenna_(test_image).png")
# Draw a diagonal blue line with thickness of 5 px
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
img = cv2.circle(img,(75,200), 75, (0,0,255), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'LAP TRINH UNG DUNG',(80,500), font, 1,(35,0,197),3,cv2.LINE_AA)
cv2.imshow('line', img)
cv2.waitKey(0)