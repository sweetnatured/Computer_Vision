import numpy as np
import cv2


resim=cv2.imread('/home/salih/Desktop/bogaz.jpg')
weight , height = resim.shape[:2]

resized_image=cv2.resize(resim,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_LANCZOS4)


cv2.imshow('a',resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()