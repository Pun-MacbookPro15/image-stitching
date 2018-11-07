import sys
import cv2
import numpy as np

img = cv2.imread("images/"+sys.argv[1])
height = np.size(img, 0)
width = np.size(img, 1)

crop_size = int(sys.argv[3])
y1 = (height-crop_size)/2
y2 = y1+crop_size

x1 = (width-crop_size)/2
x2 = x1+crop_size

#img[y1:y2,x1:x2]
crop_img = img[y1:y2, x1:x2]
#cv2.imshow("cropped", crop_img)
result_image_name = 'images/'+sys.argv[2]
cv2.imwrite(result_image_name, crop_img)
#cv2.waitKey(0)


#using command
#python crop_image.py 1.jpg c1.jpg 400