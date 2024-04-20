import numpy as np
import cv2
import random

def salt_pepper_noise(img,persentage=0.5):             # 定义函数，接受图像img和噪声比例persentage作为参数。
    img_copy = img.copy()                              # 创建一个img_copy变量，用于存储原始图像的副本。
    height,width = img_copy.shape[0:2]                 # 获取原始图像的高度和宽度。[ : 2] 表示取彩色图片的长、宽。[ : 3] 则表示取彩色图片的长、宽、通道。
    number = int(persentage * height * width)          # 计算要添加椒盐噪声的像素数量，噪声比例*图像宽度*图像高度。
    for i in range(number):                            # 循环随机生产椒盐噪声，循环次数为之前计算对的像素数量。
        x = random.randint(1,width -1)                 # 每次循环中，随机选择一个像素的坐标（x,y）。
        y = random.randint(1,height -1)
        if  random.random() < 0.5:                     # 随机生产一个值，小于0.5，则将该像素的值设为0(椒噪声）；否则设置为255(盐噪声)。
            img_copy[x,y] = 0
        else:
            img_copy[x,y] = 255
    return img_copy                                    # 返回添加了椒盐噪声额图像副本。

old_img = cv2.imread('lenna.png',2)                    # 读取lenna图像作为原始图像。

cv2.imshow('old_img',old_img)                                 # 展示原始图像
salt_pepper_noise_img = salt_pepper_noise(old_img,0.3)        # 调用函数，传入原始图像和噪声比例0.3，生产添加椒盐噪声额图像。
cv2.imshow('salt_pepper_noise_img',salt_pepper_noise_img)     # 展示添加了椒盐噪声的图像。
cv2.waitKey(0)                                                # 调用cv2.waitKey(0)来等待用户键盘输入，参数0表示持续等待直到用户按下任意键，然后关闭窗口。


