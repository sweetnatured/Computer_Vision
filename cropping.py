import numpy as np
import cv2


resim=cv2.imread('/home/salih/Desktop/bogaz.jpg')

weight , height = resim.shape[:2]

start_row , start_col = int(height*0.25) , int(weight*0.25)
end_row, end_col =  int(height*0.75) , int(weight*0.45)


cropped_image=resim[start_row:end_row , start_col:end_col]

cv2.imshow('b',cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()