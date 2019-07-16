import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('/home/hungdo/Downloads/chess2.jpeg')
gray  =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# gray = np.float32(gray)
# dst = cv2.cornerHarris(gray, 2, 3, 0.04)
#
# dst = cv2.dilate(dst, None)
#
# img[dst>0.01*dst.max()] = [0,0,255]
#
# plt.imshow(img)
# plt.show()


#Shi-Tomasi Corner
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img, (x,y), 2, 255, -1)

plt.imshow(img)
plt.show()
