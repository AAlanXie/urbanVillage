import os
import json
import numpy as np
import skimage.draw
import cv2

IMAGE_FOLDER = "./val/"
MASK_FOLOER = "./mask_val/"
PATH_ANNOTATION_JSON = './val/via_region_data.json'

# 加载VIA导出的json文件
annotations = json.load(open(PATH_ANNOTATION_JSON, 'r'))
# print(annotations)
imgs = annotations


round = 1
for imgId in imgs:
    filename = imgs[imgId]['filename']
    regions = imgs[imgId]['regions']
    if len(regions) <= 0:
        continue

    # 取出第一个标注的类别，本例只标注了一个物件
    polygons = regions[0]['shape_attributes']

    # 图片路径
    image_path = os.path.join(IMAGE_FOLDER, filename)
    # 读出图片，目的是获取到宽高信息
    image = cv2.imread(image_path)  # image = skimage.io.imread(image_path)
    height, width = image.shape[:2]

    # 创建空的mask
    maskImage = np.zeros((height,width), dtype=np.uint8)
    countOfPoints = len(polygons['all_points_x'])
    points = [None] * countOfPoints
    for i in range(countOfPoints):
        x = int(polygons['all_points_x'][i])
        y = int(polygons['all_points_y'][i])
        points[i] = (x, y)

    contours = np.array(points)

    # 遍历图片所有坐标
    for i in range(width):
        for j in range(height):
            if cv2.pointPolygonTest(contours, (i, j), False) > 0:
                maskImage[j,i] = 255

    savePath = MASK_FOLOER + filename
    # 保存mask
    cv2.imwrite(savePath, maskImage)
    print('{} is finised'.format(round))
    round = round + 1