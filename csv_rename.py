import csv
import os
import pandas as pd 

filename = "train.csv"
csv_rows = []
index = 0
with open(filename , 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        csv_rows.append(row)

for rows in csv_rows:
    if(rows[0]!='filename'):
        ls = rows[0].split(".")
        if(ls[1]=='jpg'):
            rows[0] = "image" + str(index) + '.png'
            index = index + 1

filename2= []
width = []
height = []
tclass = []
xmin = []
ymin = []
xmax = []
ymax = []

for rows in csv_rows:
    filename2.append(rows[0])
    width.append(rows[1])
    height.append(rows[2])
    tclass.append(rows[3])
    xmin.append(rows[4])
    ymin.append(rows[5])
    xmax.append(rows[6])
    ymax.append(rows[7])

df = pd.DataFrame(data = {"filename":filename2 , "width":width , "height":height , "class":tclass , "xmin":xmin , "ymin":ymin , "xmax":xmax , "ymax":ymax})
df.to_csv("./file2.csv",index = False)