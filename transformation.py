import numpy as np
import cv2


resim=cv2.imread('/home/salih/Desktop/bogaz.jpg')

weight , height = resim.shape[:2]

T_matrix=np.float32([[1,0,5],[0,1,5]])  # Creates Transformation matrix

img_transformation=cv2.warpAffine(resim,T_matrix,(height,weight)) # makes calculations between img aNd given matrix

cv2.imshow('a',img_transformation)
cv2.waitKey(0)
cv2.destroyAllWindows()
