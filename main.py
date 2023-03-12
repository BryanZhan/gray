import cv2
import numpy as np

img = cv2.imread('dog.jpg',1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
dst = np.zeros((height,width,3),np.uint8)
for i in range(height):
    for j in range(width):
        (b,g,r) = img[i,j]
        gray = int(b) * 0.144 + int(g) * 0.587 +int(r) * 0.299
        dst[i,j] = np.uint8(gray)

cv2.imshow('dog.jpg',img)
cv2.imshow('image',dst)
cv2.waitKey(0)
