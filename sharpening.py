import numpy as np
import cv2


resim=cv2.imread('/home/salih/Desktop/bogaz.jpg')


kernel=np.array([[-1,-1,-1],[-1,10,-1],[-1,-1,-1]])

sharpened=cv2.filter2D(resim,-1,kernel=kernel)

cv2.imshow('Sharpening',sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()