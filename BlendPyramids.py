import cv2
import numpy as np, sys
from  PIL import Image
from matplotlib import pyplot as plt

A = cv2.imread('/home/hungdo/Downloads/apple.jpg')
A = cv2.cvtColor(A,cv2.COLOR_BGR2RGB)
B = cv2.imread('/home/hungdo/Downloads/orange.jpeg')
B = cv2.cvtColor(B,cv2.COLOR_BGR2RGB)

# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

lpA = [gpA[5]]
for i in range(6,0,-1):
    GE = cv2.pyrUp(gpA[i])
    GE=cv2.resize(GE,gpA[i - 1].shape[-2::-1])
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)

# generate Laplacian Pyramid for B

lpB = [gpB[5]]
for i in range(6,0,-1):
    GE = cv2.pyrUp(gpB[i])
    GE = cv2.resize(GE, gpB[i - 1].shape[-2::-1])
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)

# Now add left and right halves of images in each level
LS = []
lpAc=[]
for i in range(len(lpA)):
    b=cv2.resize(lpA[i],lpB[i].shape[-2::-1])
    lpAc.append(b)
j=0
for i in zip(lpAc,lpB):
    la,lb = i
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:cols//2], lb[:,cols//2:]))
    j=j+1
    LS.append(ls)

ls_ = LS[0]
for i in range(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_= cv2.resize(ls_, LS[i].shape[-2::-1])
    ls_ = cv2.add(ls_, LS[i])

# image with direct connecting each half
B= cv2.resize(B, A.shape[-2::-1])
real = np.hstack((A[:,:cols//2],B[:,cols//2:]))

cv2.imwrite('Pyramid_blending2.jpg',ls_)
cv2.imwrite('Direct_blending.jpg',real)
# Image.fromarray(real).show()
plt.subplot(121),plt.imshow(ls_)
plt.title('Pyramid_blending2'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(real)
plt.title('Direct_blending'), plt.xticks([]), plt.yticks([])
plt.show()