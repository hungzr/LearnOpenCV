import  numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/home/hungdo/Downloads/chess1.jpeg',0)

# Initiate FAST object with default values
fast = cv2.FastFeatureDetector_create()

#find and draw keypoints
kp = fast.detect(img, None)
img2 = cv2.drawKeypoints(img, kp,None, color=(255,0,0))

#print all default params
print("Threshold",fast.getThreshold())
print("nonmaxSuppression",fast.getNonmaxSuppression())
print("neighborhood",fast.getType())
print("Total keypoints with nonmaxSuppression",len(kp))

# plt.title("fast_true"), plt.imshow(img2)

#Disable nonmaxSuppression
fast.setNonmaxSuppression(False)
kp = fast.detect(img, None)

print("Total keypoints without nonmaxSuppression",len(kp))
img3 = cv2.drawKeypoints(img, kp,None, color=(255,0,0))

# plt.title("fast_false"), plt.imshow(img3)

plt.subplot(121),plt.imshow(img2)
plt.title('fast_true'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img3)
plt.title('fast_false'), plt.xticks([]), plt.yticks([])

plt.show()