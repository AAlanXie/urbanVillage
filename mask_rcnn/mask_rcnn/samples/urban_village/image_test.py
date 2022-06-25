from PIL import Image
import os

IMAGES_PATH = '/Volumes/Seagate/Xiamen_map/'  # 图片集地址
DIR = '/Volumes/Seagate/Xiamen_map/'

image_names = [name for name in os.listdir(IMAGES_PATH)]

# image = Image.open(DIR + picture_name)


# print(image.size)

# n1 = str(image_names[1])[3:].split('-')[0]
# n2 = str(image_names[2])[3:].split('-')[1].split('.')[0]
# print(n1)
# print(n2)



print(type(image_names[0]))
