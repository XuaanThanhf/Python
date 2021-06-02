import cv2
cap = cv2.VideoCapture('face-demographics-walking.mp4',0)
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    cv2.imshow('frame', frame)
    if cv2.waitKey(60) & 0xFF == ord('q'):
      break
  else: 
    break
cap.release()
cv2.destroyAllWindows()
