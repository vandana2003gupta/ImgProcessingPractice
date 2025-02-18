import cv2
import numpy as np

img = cv2.imread("./images/fruits.png")

print(img.shape)
print(type(img))
print(img)

## Gray Scale Image ##
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(img_gray.shape)
# print(type(img_gray))
# cv2.imshow("window",img_gray)

## Stack of RGB Shades ##
# blue= img[:,:,1]
# green = img[:,:,2]
# black = img[:,:,0]
# new_img = np.hstack((blue, green, black))
#new_img = np.dstack((blue, green, black))
#cv2.imshow("img", new_img)

## RESIZE ##
# img_resize = cv2.resize(img, (200, 100))
# print(img_resize)
# cv2.imshow("window", img_resize)

## Image Flip ##
#img_flip = cv2.flip(img, 1)
# img_flip = cv2.flip(img, 0)
#img_flip = cv2.flip(img, -1)
#cv2.imshow("window",img_flip)


#img_crop = new_img[100:800, 100:800]
#img_crop = img[100:200, 100:200]
# cv2.imshow("img_crop", img_crop)

cv2.imshow("window", img)
cv2.waitKey(0)

