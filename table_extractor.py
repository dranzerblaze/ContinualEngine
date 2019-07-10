import csv
import random
import os
import pandas as pd
import cv2

filename = "file.csv"
csv_rows = []
with open(filename , 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        csv_rows.append(row)

for index,rows in enumerate(csv_rows):
    if(rows[0]!='name'):
        img_name = rows[0]
        x_min = rows[1]
        x_max = rows[2]
        y_min = rows[3]
        y_max = rows[4]
        dir_path = '/media/bhams/Stuff/table/dataset/images/'
        img_path = dir_path + img_name
        img = cv2.imread(img_path)
        crop_img = img[int(y_min) : int(y_max), int(x_min):int(x_max)]
        if(int(y_max) - int(y_min) !=0 and int(x_max) - int(x_min) !=0):
            cv2.imwrite("{}.png".format(index),crop_img)
            print (img_name)

        

