import numpy as np
import cv2
from skimage import util
import random

# 定义一个名为'gauss_noise'的函数，该函数接收图像img以及高斯噪声的均值(mean)、标准差(sigma)和噪声比例(percentage)作为参数。
def gauss_noise(img,mean=2,sigma=4,percentage=2):
    img_copy = img.copy()                                  # 创建一个img_copy变量，用于存储原始图像额副本。
    height,width = img.shape[0:2]                          # 获取原始图像的高度和宽度。
    number = int(width * height * percentage)              # 计算需要添加高斯噪声对的像素数量，这里是图像宽度*高度*噪声比例。
    for i in range(number):                                # 通过循环生产高斯噪声，循环次数为之前计算对的像素数量。
        x = random.randint(0,width -1)                     # 每次循环中，随机选择一个像素额坐标（x,y)
        y = random.randint(0,height -1)                    # random.randint(a, b)用于生成一个指定范围内的整数，其中a和b分别表示生成随机整数的最小值和最大值
        img_copy[x,y] = img_copy[x,y] + random.gauss(mean,sigma)  # 将该像素对的灰度值增加一个均值和标准为参数对的高斯分布中随机选取的值（random.gauss(mean,sigma) ）
        if img_copy[x,y] > 255:                            # 若像素值超过255，将其截断为255，若像素值小于0，将其设置为0。
            img_copy[x,y] = 255
        elif img_copy[x,y] < 0:
            img_copy[x,y] = 0
    return img_copy                                        # 返回添加了高斯噪声的副本图像。

old_img = cv2.imread("lenna.png",2)                        # 读取原始图像，2为原深度图像；0为将图像转化为灰图；4为原颜色图像；-1为取值，Alpha通道加载图像。

new_img = gauss_noise(old_img,2,4,5)                       # 调用函数，传入原始图像，均值2，标准差4和噪声比例5，生成添加了高斯噪声的图像。

cv2.imshow('old_img',old_img)                              # 展示原始图像和添加了高斯噪声的图像。
cv2.imshow('gauss_noise_img',new_img)
cv2.waitKey(0)                                             # 调用cv2.waitKey(0)来等待用户键盘输入，参数0表示持续等待直到用户按下任意键，然后关闭窗口。
















