import numpy as np
import cv2

cap = cv2.VideoCapture(0) # pass device index or video path

while(True):
    # Capture frame-by-frame 
    # return boolean if read correctly, 
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    k = cv2.waitKey(1) 
    if k & 0xFF == ord('q'):
        break
    if k & 0xFF == ord('p'):
    	# can get properties of a video by passing propid
		# number 0-18 represents a property to get
		print cap.get(1)

# can see if cap iniitlaized capture
# cap.isOpened() returns boolean
# otehrwise open using cap.open()

# can set properties with cap.set(propId, value)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()