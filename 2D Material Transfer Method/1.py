from PIL import Image
import numpy as np
import cv2
import os
import itertools

image_dir = r"/Users/xiechangen/Downloads/20251211_03"
output_dir = r"/Users/xiechangen/Desktop/output1/3"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# monolayer
brightlower = np.array([117,134,200])   
brightupper = np.array([119,158,211]) 

# bilayer
darklower = np.array([115,159,192]) 
darkupper = np.array([117,175,215]) 

img = cv2.imread(r"/Users/xiechangen/Downloads/20251211_01＿input/VHX_graphene000027.jpg")
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

output1 = cv2.inRange(hsv_img, brightlower, brightupper)
contours1, hierarchy1 = cv2.findContours(output1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # cv2.RETR_EXTERNAL 表示取得範圍的外輪廓座標串列，cv2.CHAIN_APPROX_SIMPLE 為取值的演算法

output2 = cv2.inRange(hsv_img, darklower, darkupper)
contours2, hierarchy2 = cv2.findContours(output2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours1:
    area = cv2.contourArea(contour)
    color = (0,0,255)
    if(area > 3000):
        # 取得原座標與長寬尺寸
        x, y, w, h = cv2.boundingRect(contour)                      
        print("淺色中心 = ({},{})".format((x+0.5*w)*10//71,(2160-y-0.5*h)*10//71))
        img = cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)  # 繪製四邊形
        
        # 定義要標記的字串和位置
        text = ("({},{})".format((x+0.5*w)*10//71,(2160-y-0.5*h)*10//71))
        
        # 計算文字的大小
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        thickness = 2
        (text_width, text_height) = cv2.getTextSize(text, font, font_scale, thickness)
        
        # 在指定位置繪製文字
        org = (int(x+0.5*w), int(y+0.5*h))  # 文字的起始位置
        color = (0, 0, 255)  # 文字的顏色 (BGR)
        cv2.putText(img, text, org, font, font_scale, color, thickness)
cv2.imwrite("/Users/xiechangen/Downloads/output"+"_test.jpg", img)

for contour in contours2:
    area = cv2.contourArea(contour)
    color = (0,255,0)
    if(area > 3000):
        # 取得原座標與長寬尺寸
        x, y, w, h = cv2.boundingRect(contour)                      
        print("深色中心 = ({},{})".format((x+0.5*w)*10//71,(2160-y-0.5*h)*10//71))
        img = cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)  # 繪製四邊形
        
        # 定義要標記的字串和位置
        text = ("({},{})".format((x+0.5*w)*10//71,(2160-y-0.5*h)*10//71))
        
        # 計算文字的大小
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        thickness = 2
        (text_width, text_height) = cv2.getTextSize(text, font, font_scale, thickness)
        
        # 在指定位置繪製文字
        org = (int(x+0.5*w), int(y+0.5*h))  # 文字的起始位置
        color = (0, 255, 0)  # 文字的顏色 (BGR)
        cv2.putText(img, text, org, font, font_scale, color, thickness)
         
cv2.imwrite("/Users/xiechangen/Downloads/output"+"_test.jpg", img)
