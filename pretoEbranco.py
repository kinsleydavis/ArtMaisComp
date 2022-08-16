import cv2
import os
 
path = 'c:/pretoEbranco/'
 
for x in os.listdir():
    if x.endswith(".jpg") or x.endswith(".png"):      
        image = cv2.imread(path + x)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Original image',image)
        cv2.imshow('Gray image', gray)
        cv2.imwrite(path + x,gray)
        print(x)


cv2.waitKey(0)
cv2.destroyAllWindows()
