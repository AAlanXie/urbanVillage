import PIL.Image as Image
import os
 
IMAGES_PATH = '/Volumes/Seagate/Xiamen_map_identify/'  # 图片集地址
IMAGE_WEIGHT = 1003  # 每张小图片的宽
IMAGE_HEIGHT = 1039  #每张图片的高
IMAGE_ROW =  3 # 图片间隔，也就是合并成一张图后，一共有几行
IMAGE_COLUMN = 50  # 图片间隔，也就是合并成一张图后，一共有几列
IMAGE_SAVE_PATH = '/Volumes/Seagate/Xiamen_mask_test.png'  # 图片转换后的地址
 
# 获取图片集地址下的所有图片名称
image_names = [name for name in os.listdir(IMAGES_PATH)]


# 简单的对于参数的设定和实际图片集的大小进行数量判断
print(len(image_names))

if len(image_names) != IMAGE_ROW * IMAGE_COLUMN:
    print("error!")
 
# 定义图像拼接函数
def image_compose():
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_WEIGHT, IMAGE_ROW * IMAGE_HEIGHT)) #创建一个新图
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):

            from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
                (IMAGE_WEIGHT, IMAGE_HEIGHT),Image.ANTIALIAS)

            n1 = (int((str(image_names[IMAGE_COLUMN * (y - 1) + x - 1])[3:].split('-')[0]))-1) * IMAGE_HEIGHT

            n = str(image_names[IMAGE_COLUMN * (y - 1) + x - 1])[3:].split('-')[1].split('.')[0]

            n2 = (int(n) - 1) * IMAGE_WEIGHT


            to_image.paste(from_image, (n2, n1))
    return to_image.save(IMAGE_SAVE_PATH) # 保存新图
    
image_compose()
