# -*- coding: utf-8 -*-
#
# Usage: $ python image_converter.py [input_dir_path] [output_dir_path]
#
import sys
import cv2
import numpy as np
import os
import glob
import re

args = sys.argv

if(len(args) < 2):
    print("Usage: $ python ImageConverter.py [image_file_path] [save_path]")

def make_contour_image(input_path, output_path):
    kernel = np.ones((5,5),np.uint8)

    gray = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    cv2.imwrite("gray.jpg", gray)

    dilated = cv2.dilate(gray, kernel, iterations=1)
    cv2.imwrite("dilated.jpg", dilated)

    diff = cv2.absdiff(dilated, gray)
    cv2.imwrite("diff.jpg", diff)

    contour = 255 - diff
    cv2.imwrite(output_path, contour)

    os.remove("gray.jpg")
    os.remove("dilated.jpg")
    os.remove("diff.jpg")

#args[1]: input, args[2]: output
org_path = args[1]
dst_path = args[2]

#ファイル取得
files = os.listdir(org_path)
file_num = len(files)

#jpgのみ
pattern = r"jpg"

for i in range(1, file_num+1):
    filename = files[i-1]
    matchOB = re.search(pattern , filename)    
    if matchOB:
        make_contour_image(org_path+filename, dst_path+filename)
        print(i, '/', file_num, ' is done.')
