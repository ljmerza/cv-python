import numpy as np
import cv2

# Load two images
img1 = cv2.imread('cv-1.jpg')
img2 = cv2.imread('opencv.png')

# I want to put logo on top-left corner, So I create a ROI
# get number of rows, columns, and channels (3 for bgr)
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]
print 'roi: ', roi

# Now create a mask of logo and create its inverse mask also
# covert to grey scale
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow('img2gray',img2gray)

# filter out pixels based off threshold
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('mask',mask) # image we want

# invert image
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask_inv',mask_inv)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
cv2.imshow('img1_bg',img1_bg)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
cv2.imshow('img2_fg',img2_fg)

# Put logo in ROI and modify the main image
img1[0:rows, 0:cols ] = cv2.add(img1_bg,img2_fg)

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()