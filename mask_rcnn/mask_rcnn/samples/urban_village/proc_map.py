from PIL import Image
import shutil
import os
import random


#  图片切割
PATCH_SIZE = 512
DIR = '/Volumes/Seagate/Xiamen_map'

if os.path.exists(DIR):
    shutil.rmtree(DIR)
os.mkdir(DIR)

# 载入图片
img = Image.open('/Volumes/Seagate/Xiamen_Level_19.tif')


width, height = img.size  # Get dimensions
print(img.size)

cnt = 0
for x in range(0, height, PATCH_SIZE):
    for y in range(0, width, PATCH_SIZE):
        cnt += 1


for top in range(0, height, PATCH_SIZE):
    for left in range(0, width, PATCH_SIZE):

        patch = img.crop((left, top, left + PATCH_SIZE, top + PATCH_SIZE))
        # patch.show()


        fn = '/Volumes/Seagate/Xiamen_map'+ str(top) + "_" + str(left) + '.tif'
        patch.save(fn) 

        # print('{0} row {1} columns of picture is generating'.format(row, column))


print('{0} patches of size {1} are generated.'.format(cnt, PATCH_SIZE))
print('Done.')