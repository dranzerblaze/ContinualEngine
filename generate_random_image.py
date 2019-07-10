from PIL import Image,ImageDraw,ImageFont
import random
import string
from google_images_download import google_images_download
import os
import cv2
import numpy as np 
import pandas as pd
from collections import namedtuple

table_filename = []
table_height = []
table_width = []
table_class = []
table_xmin = []
table_xmax = []
table_ymin = []
table_ymax = []
Rectangle = namedtuple('Rectangle' , 'xmin ymin xmax ymax')

#Checks whether a new table intercects with previous tables or not
def area(a,b):
    for ls in range(0,len(a)):
        dx = min(a[ls].xmax , b.xmax) - max(a[ls].xmin , b.xmin)
        dy = min(a[ls].ymax , b.ymax) - max(a[ls].ymin , b.ymin)
        if(dx >=0 and dy>=0):
            return False
    return True

def random_text_gen(length = 10):
    letter = string.ascii_letters + string.digits 
    return ''.join(random.sample(letter , length))

def text_wrap(text,font,max_width):
    lines = []
    divide = random.randrange(1,3)
    max_width = max_width / divide
    if font.getsize(text)[0] <= max_width:
        lines.append(text)
    else:
        words = text.split(' ')
        i = 0
        while i < len(words):
            line = ''
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:                
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            lines.append(line)    
    return lines

def image_gen(j):
    img = Image.new('RGB' , (1500,2000) , color = (255,255,255))
    fnt = ImageFont.truetype('roboto.ttf' , random.randrange(20,40))
    d = ImageDraw.Draw(img)
    x = 10
    y = 10
    
    for i in range(1,100):
        random_text = random_text_gen(25)*random.randrange(0,3)
        line_height = fnt.getsize('hg')[1]
        align_var = random.randrange(0,3)
        if(align_var==0):
            align_style = "left"
        elif(align_var == 1):
            align_style = "right"
        else:
            align_style = "center"
        d.multiline_text((x,y) , random_text , font = fnt , fill = (0,0,0),align = 'left' )
        y = y + line_height
    filename = str(j) + '.png'
    img.save(filename)
    dir = os.getcwd() + '/table_images/'
    no_of_tables = random.randrange(1,5)
    image_numbers = []
    rectangles = []
    for number in range(0,no_of_tables):
        image_numbers.append(random.randrange(0,180))
    for number in image_numbers:
        #print (number)
        img_path = dir + str(number) + '.png'
        small_img = cv2.imread(img_path)
       # print(small_img.shape)
        row ,col = small_img.shape[:2]
        bottom = small_img[row-2:row , 0:col]
        border_size = random.randrange(2,20)
        small_img = cv2.copyMakeBorder(small_img , top = border_size ,bottom = border_size , left = border_size , right = border_size , borderType = cv2.BORDER_CONSTANT , value = [255,255,255])
        #cv2.imshow('im',small_img)
        large_image = cv2.imread(filename)
       # print(large_image.shape)
        x_offset = random.randrange(0,1500 - small_img.shape[1])
        y_offset = random.randrange(0,2000 - small_img.shape[0])
        ra = Rectangle(x_offset , y_offset , x_offset+small_img.shape[1] , y_offset+small_img.shape[0])
        if(len(rectangles) == 0 or area(rectangles , ra) == True):
            large_image[y_offset:y_offset + small_img.shape[0] , x_offset:x_offset + small_img.shape[1]] = small_img
            ra = Rectangle(x_offset , y_offset , x_offset+small_img.shape[1] , y_offset+small_img.shape[0])
            rectangles.append(ra)
           # print (rectangles)
            cv2.imwrite(filename , large_image)
            table_filename.append(str(j)+'.png')
            table_class.append("table")
            table_height.append(2000)
            table_width.append(1500)
            table_xmin.append(x_offset)
            table_ymin.append(y_offset)
            table_xmax.append(x_offset + small_img.shape[1])
            table_ymax.append(y_offset + small_img.shape[0])

for i in range(0,2):
    image_gen(i)
    print ("Image Done = " + str(i+1))
df = pd.DataFrame(data = {"name":table_filename , "xmin":table_xmin , "xmax":table_xmax , "ymin":table_ymin , "ymax":table_ymax , "class":table_class , "height":table_height , "width":table_width})
df.to_csv("./file2.csv" , index = False)
