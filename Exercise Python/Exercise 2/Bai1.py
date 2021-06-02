import cv2
img = cv2.imread("Lenna_(test_image).png",0)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()