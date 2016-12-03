import numpy as np
import cv2
from matplotlib import pyplot as plt

# load a color image in grayscale
img = cv2.imread('cv-1.jpg', 0)

cv2.imshow('image', img)

# wait x number of milliseconds for keyboard entry - 0 = infinite
k = cv2.waitKey(0) & 0xFF # for x64 add 0xFF

if k == 27: # esc key
	cv2.destroyAllWindows() # use destroyWindow() to kill specific window
elif k == ord('s'): # s key
	# write an image to disk
	cv2.imgwrite('cv-1.png', img)
	cv2.destroyAllWindows()



########################
# matplot lib
#########################
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

# wait x number of milliseconds for keyboard entry - 0 = infinite
k = cv2.waitKey(0) & 0xFF # for x64 add 0xFF

if k == 27: # esc key
	cv2.destroyAllWindows() # use destroyWindow() to kill specific window
elif k == ord('s'): # s key
	# write an image to disk
	cv2.imgwrite('cv-1.png', img)
	cv2.destroyAllWindows()


# OpenCV follows BGR order, while matplotlib likely follows RGB order.
# need to convert to display opencv image in matplotlib
img = cv2.imread('cv-1.jpg')

b,g,r = cv2.split(img) # split bgr colors
img2 = cv2.merge([r,g,b]) # merge them back but into rgb order

plt.subplot(121);plt.imshow(img) # expects distorted color
plt.subplot(122);plt.imshow(img2) # expect true color
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()