import cv2
import numpy as np

img1 = cv2.imread("hat.png")
img2= cv2.imread("blood.jpg")

# vis = np.concatenate((img1, img2), axis=1)
# cv2.imwrite('out.png', vis)

h1, w1 = img1.shape[:2]
h2, w2 = img2.shape[:2]

vis = np.zeros((max(h1, h2), w1+w2,3), np.uint8)

#combine 2 images
vis[:h1, :w1,:3] = img1
vis[:h2, w1:w1+w2,:3] = img2
cv2.imwrite('out.png', vis)
