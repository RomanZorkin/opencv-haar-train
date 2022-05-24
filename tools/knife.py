import cv2,time
from pathlib import Path

im_path = Path('tmp/crush/base')
images = [image for image in im_path.iterdir()]

num = 0
for image in images:
    img = cv2.imread(str(image))
    img2 = img
    height, width, channels = img.shape
    # Number of pieces Horizontally 
    CROP_W_SIZE  = 11
    # Number of pieces Vertically to each Horizontal  
    CROP_H_SIZE = 11
    for ih in range(CROP_H_SIZE ):
        for iw in range(CROP_W_SIZE ):

            x = int(width/CROP_W_SIZE * iw )
            y = int(height/CROP_H_SIZE * ih)
            h = int((height / CROP_H_SIZE))
            w = int((width / CROP_W_SIZE ))
            print(x,y,h,w)
            img = img[y:y+h, x:x+w]

            NAME = str(time.time()) 
            cv2.imwrite("tmp/crush/crush/bg" + str(num) +  ".jpg",img)
            img = img2
            num += 1