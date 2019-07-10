import os
import glob
import pandas as pd 
import argparse
import xml.etree.ElementTree as et 
import cv2

def xmt_to_csv(path):
    name_list = []
    xmin = []
    xmax = []
    ymin = []
    ymax = []
    height = []
    width = []
    for image in glob.glob(path + '/*.jpg'):
        path2 = glob.glob(path + '/*.jpg')
        img = cv2.imread(path2[0])
        dimen = img.shape
        print(dimen)
        print(path2)
        xml_file = glob.glob(path + '/*.xml')
        print(xml_file)
        tree = et.parse(xml_file[0])
        root = tree.getroot()
       
        file_name = root.attrib["filename"]
        for member in root.findall('table'):
            x = []
            y = []
            str = member[0].attrib["points"]
            lst = str.split()
            for ls in lst:
                bs = ls.split(",")
                x.append(int(bs[0]))
                y.append(int(bs[1]))
            name_list.append(file_name)
            xmin.append(min(x))
            xmax.append(max(x))
            ymin.append(min(y))
            ymax.append(max(y))
            height.append(dimen[0])
            width.append(dimen[1])
        
    df = pd.DataFrame(data = {"name":name_list , "xmin":xmin , "xmax":xmax , "ymin":ymin ,"ymax":ymax , "height":height , "width":width})
    df.to_csv("./file.csv",index = False)
            

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

    xmt_to_csv(args.inputDir)
        # xml_df.to_csv(
        #     args.outputFile, index=None)
        # print('Successfully converted xml to csv.')

if __name__ == '__main__':
    main()
