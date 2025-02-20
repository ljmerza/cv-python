import numpy as np
import cv2

# create black image
img = np.zeros((512,512,3), np.uint8)

# draw diagnal blue line with thickness 5px
# imae to draw on, from 0,0 to 511,511
img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

# 
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# center coordinates and radius
img = cv2.circle(img,(447,63), 63, (0,0,255), -1)

# center coordinates, axes lengths, start/end arcs
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

#polygon - need coordinates of vertices
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))