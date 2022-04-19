import cv2
import numpy as np

def nothing(x):
    pass

    img=np.zeros((550,550,3),np.uint8)
    cv2.namedWindow('img')

    cv2.createTrackbar('R','image',0,255,nothing)
    cv2.createTrackbar('G','image',0,255,nothing)
    cv2.createTrackbar('B','image',0,255,nothing)
    
    switch='0 : KAPA \n1:AC'
    cv2.createTrackbar(switch, 'image',0,1,nothing)

    while(1):
        cv2.imshow('image',img)
        k=cv2.waitKey(1)&0xFFFF
        if k==27:
            break