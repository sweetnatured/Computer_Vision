import numpy as np
import cv2


resim=cv2.imread('/home/salih/Desktop/bogaz.jpg')

weight , height = resim.shape[:2]

trans_matrix=cv2.getRotationMatrix2D((weight/2,height/2),2 0,1)

rotated_matrix=cv2.warpAffine(resim,trans_matrix,(height,weight))

cv2.imshow('a',rotated_matrix)
cv2.waitKey(0)
cv2.destroyAllWindows()