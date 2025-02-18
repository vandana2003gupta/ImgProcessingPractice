import cv2
import numpy as np

img = cv2.imread("./images/fruits.png")

print(img.shape)
print(type(img))
print(img)

cv2.imshow("window",img)
cv2.waitKey(0)
