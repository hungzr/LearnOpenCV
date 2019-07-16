import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('/home/hungdo/Downloads/chess1_1.jpeg',0)
img2 = cv2.imread('/home/hungdo/Downloads/chess1.jpeg',0)

#inittiate SIFT detector
orb = cv2.ORB_create()

#find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# #create BFMatcher object
# bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, crossCheck=True)
#
# #Match descriptors
# matches = bf.match(des1, des2)
#
# #Sort them in the order of their distance
# matches = sorted(matches, key=lambda  x:x.distance)
#
# #Draw first 10 matches
# img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)

#######################################
bf = cv2.BFMatcher_create()
matches = bf.knnMatch(des1, des2, k=2)

#Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)

plt.imshow(img3), plt.show()