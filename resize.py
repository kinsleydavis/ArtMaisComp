import cv2
def split_frames(filename, output_str):
    capture = cv2.VideoCapture(filename)
    i = 0
    while(capture.isOpened()):
        ret, frame = capture.read()  
        if ret == False:
            break
        if i == 20:
            break    
        cv2.imwrite(output_str.format(i),frame)
        i += 1
    capture.release()
split_frames('xilogravura.mp4', 'frame-{}.jpg')
src = cv2.imread('frame-{}.jpg', cv2.IMREAD_UNCHANGED)
#percent by which the image is resized
scale_percent = 50
#calculate the 50 percent of original dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)
# dsize
dsize = (width, height)
# resize image
output = cv2.resize(src, dsize)
cv2.imwrite('D:/cv2-resize-image-50.png',output) 
cv2.imwrite('c:/ArteMaisComp/novo_frame={}.jpg',output) 
cv2.destroyAllWindows()




