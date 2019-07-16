import cv2
from PIL import Image
import  numpy as np
from matplotlib import pyplot as plt


# cap = cv2.VideoCapture('/home/hungdo/thanhdt_video/2019-06-12/LLQ1/12-48/output-00000-00120.mp4')
#
#
# while(cap.isOpened()):
#     # Capture frame by frame
#     ret, frame = cap.read()
#
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     #Display result frame
#     # cv2.imshow('frame', gray)
#     # Image.fromarray(gray).show()
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

img_1 = Image.open('/home/hungdo/thanhdt/2019-06-09/NVL1/output-00480-00600.mp4-095.jpg')
# # cv2.imshow('test', img)
img_2 = Image.open('/home/hungdo/thanhdt/2019-06-09/NVL1/output-00480-00600.mp4-096.jpg')
# #
img_1 = np.copy(img_1)
img_2  = np.copy(img_2)

test_img = cv2.imread('/home/hungdo/Downloads/sudoku.jpeg',0)
test_img = cv2.medianBlur(test_img,1)
rows, cols = test_img .shape

print('rows: {0} ,cols: {1} '.format(rows,cols))
# # print(type(img))
# Image.fromarray(img_1).show()
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# px = img[100,100]
# b = cv2.split(img)
# print(b)
# img = cv2.merge((b))
img = cv2.addWeighted(img_1,1,img_2,0.3,0.3)
# Image.fromarray(img).show()
# print(px)


ret , thresh1 = cv2.threshold(test_img,127,255, cv2.THRESH_BINARY)
# ret , thresh2 = cv2.threshold(test_img,127,255, cv2.THRESH_BINARY_INV)
# ret , thresh3 = cv2.threshold(test_img,127,255, cv2.THRESH_TRUNC)
# ret , thresh4 = cv2.threshold(test_img,127,255, cv2.THRESH_TOZERO)
# ret , thresh5 = cv2.threshold(test_img,127,255, cv2.THRESH_TOZERO_INV)
th2 = cv2.adaptiveThreshold(test_img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(test_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)


titles = ['Original','Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [test_img, thresh1, th2, th3]

# for i in range(4):
#     plt.subplot(2,2,i+1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
#
# plt.show()

#####################################
# get edge by using Candy Edge Detection
img = cv2.imread('/home/hungdo/thanhdt/2019-06-09/NVL1/output-00480-00600.mp4-096.jpg',0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()