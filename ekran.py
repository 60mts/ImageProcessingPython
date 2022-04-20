import numpy

img=np.zeros((700,700,3),np.uint8)
cv2.line(img,(100,0),(100,700),(0,0,255),5)
cv2.imshow("ekran",img)
cv2.waitKey(0)

