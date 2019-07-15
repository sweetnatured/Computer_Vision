import cv2
import numpy as np

resim=cv2.imread('/home/salih/Desktop/res.jpg')
cv2.imshow('original',resim)
cv2.waitKey(0)

kernel_ones=np.ones((5,5))

erosion=cv2.erode(resim,kernel=kernel_ones,iterations=3)   # iteration number gives quantity of thickness
cv2.imshow('Erosion',erosion)
cv2.waitKey(0)


dilation=cv2.dilate(resim,kernel_ones,iterations=3)   # iteration number gives quantity of thinness
cv2.imshow('Dilation',dilation)
cv2.waitKey(0)


opening=cv2.dilate(erosion,kernel_ones,iterations=1)
closing=cv2.erode(dilation,kernel_ones,iterations=1)

cv2.imshow('Opening',opening)          #first erosion then dilation
cv2.imshow('Closing',closing)          #first dilation then erosion

cv2.waitKey(0)




cv2.destroyAllWindows()
