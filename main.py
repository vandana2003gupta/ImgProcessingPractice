import cv2
import numpy as np

# img = cv2.imread("./images/fruits.png")
#
# print(img.shape)
# print(type(img))
# print(img)

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

##Crop Image ##
#img_crop = new_img[100:800, 100:800]
#img_crop = img[100:200, 100:200]
# cv2.imshow("img_crop", img_crop)

#img_write = cv2.imwrite("OrangeColoured.png", img)

## Shapes ##
# img= np.zeros((512,512,3))
# cv2.rectangle(img, pt1= (100,100), pt2= (300,300), color=(255,0,0), thickness=-1)
# cv2.rectangle(img, pt1= (100,100), pt2= (300,300), color=(0,255,0), thickness=3)
# cv2.circle(img, center= (100,400), radius=50, color=(0, 255,0), thickness=3)
# cv2.circle(img, center= (100,400), radius=50, color=(0, 0,255), thickness=-1)
# cv2.line(img,pt1=(0,0), pt2=(512,512), color=(0,255,0),thickness=3)
# cv2.putText(img, text=" Hey Utk!", org=(310,310),fontScale=2,fontFace= cv2.FONT_HERSHEY_PLAIN,color=(0,0,255),thickness=3 )


def draw(event, x,y, flags, param):
    # print("Event Triggered")
    # print(event)
    if event ==0:
        print("Mouse Moved")
    if event==1:
        print("Mouse Right Clicked")
cv2.namedWindow(winname='window')
cv2.setMouseCallback("window", draw)

img = np.zeros((512,512,3))

while True:
    cv2.imshow("window",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()



# cv2.imshow("window", img)
# cv2.waitKey(0)

