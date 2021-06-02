import cv2

IMG_PATH = 'Lenna_(test_image).png'

# read image
img = cv2.imread(IMG_PATH)
print(IMG_PATH, img.shape)


w = 2
h = 1/4
img_resized = cv2.resize(src=img, dsize=None, fx=w, fy=h)
reisze_img = 'Lenna: w*%.1f-h*%.2f.jpg' % (w, h)
cv2.imwrite(reisze_img, img_resized)
print(reisze_img, img_resized.shape)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
