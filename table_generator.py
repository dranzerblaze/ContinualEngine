import os
import glob
import pandas as pd
import random
import xml.etree.ElementTree as et
import cv2
import argparse
from PIL import Image

def xml_to_csv(path):
    
    for image in glob.glob(path + '/*.jpg'):
        img_path = glob.glob(path + '/*.jpg')
        img = cv2.imread(img_path[0])
        img_dimensions = cv2.imread(img_path[0])
        img_dimensions = img.shape
        height = img_dimensions[0]
        width = img_dimensions[1]
        #print (img_dimensions)
        xml_path = glob.glob(path + '/*.xml')
        tree = et.parse(xml_path[0])
        root = tree.getroot()
        filename = root.attrib["filename"]
        table_filename = []
        table_class = []
        table_height = []
        table_width = []
        table_x_min = []
        table_x_max = []
        table_y_min = []
        table_y_max = []
        for member in root.findall('table'):
            str = member[0].attrib["points"]
            x = []
            y = []
            lst = str.split()
            for ls in lst:
                bs = ls.split(",")
                x.append(bs[0])
                y.append(bs[1])
            table_filename.append(filename)
            table_height.append(height)
            table_width.append(width)
            table_class.append("table")
            table_x_min.append(min(x))
            table_x_max.append(max(x))
            table_y_min.append(min(y))
            table_y_max.append(max(y))
    df = pd.DataFrame(data = {"name":table_filename , "xmin":table_x_min , "xmax":table_x_max , "ymin":table_y_min , "ymax":table_y_max , "class":table_class})
    df.to_csv("./file.csv" , index = False)

            
            


def main():
    # Initiate argument parser
    parser = argparse.ArgumentParser(
        description="Sample TensorFlow XML-to-CSV converter")
    parser.add_argument("-i",
                        "--inputDir",
                        help="Path to the folder where the input .xml files are stored",
                        type=str)
    parser.add_argument("-o",
                        "--outputFile",
                        help="Name of output .csv file (including path)", type=str)
    args = parser.parse_args()

    if(args.inputDir is None):
        args.inputDir = os.getcwd()
    if(args.outputFile is None):
        args.outputFile = args.inputDir + "/labels.csv"

    assert(os.path.isdir(args.inputDir))

    xml_to_csv(args.inputDir)
        # xml_df.to_csv(
        #     args.outputFile, index=None)
        # print('Successfully converted xml to csv.')

if __name__ == '__main__':
    main()
