import cv2
from PIL import Image 
for i in range(1,10):
    im = Image.open('kinsley' + str(i) + '.jpg')
    im = im.crop( (100, 100, 356, 356) ) 
    im.save('novo' + str(i) + '.jpg') 
# im.show()