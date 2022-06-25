import glob
import os
from PIL import Image

IMAGES_PATH = 'D:/Code/Python-DeepLearning/My_Mask_Rcnn/Mask_RCNN-2.0/urban_village/test_Xia_mask'  # 图片集地址

for name in os.listdir(IMAGES_PATH):

	image = Image.open(name) # open color image
	pixdata = image.load()

	for y in range(0, 512):
		for x in range(0, 512):
			color = image.getpixel((x,y))
			if color != (255,0,0,255):
				image.putpixel((x, y), (0,0,0,255))
			else:
				image.putpixel((x, y), (255,255,255,255))


	image.save(name)