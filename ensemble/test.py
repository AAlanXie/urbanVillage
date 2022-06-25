import numpy as np
import cv2

height = 512
weight = 512

maskImage = np.zeros((height,weight), dtype=np.uint8)

for i in range(height):
    for j in range(weight):
        if i > 100 and i < 300:
            maskImage[i,j] =  255

savePath = './test.jpg'

cv2.imwrite(savePath, maskImage)
