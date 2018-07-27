import os
import numpy as np
import cv2
import argparse
import re

parser = argparse.ArgumentParser('create image pairs')
parser.add_argument('--fold_A', dest='fold_A', help='input directory for image A', type=str, default='../dataset/50kshoes_edges')
parser.add_argument('--fold_B', dest='fold_B', help='input directory for image B', type=str, default='../dataset/50kshoes_jpg')
parser.add_argument('--fold_AB', dest='fold_AB', help='output directory', type=str, default='../dataset/test_AB')

args = parser.parse_args()

for arg in vars(args):
    print('[%s] = ' % arg,  getattr(args, arg))

pattern = ".jpg"
    
splits = os.listdir(args.fold_A)

print(splits)


for sp in splits:
    matchOB = re.search(pattern, sp)
    if(matchOB):
        path_A = os.path.join(args.fold_A, sp)
        path_B = os.path.join(args.fold_B, sp)
        path_AB = os.path.join(args.fold_AB, sp)
        #if not os.path.isdir(path_AB):
        #    os.makedirs(path_AB)        
        print(path_A)
        print(path_B)
        im_A = cv2.imread(path_A)        
        im_B = cv2.imread(path_B)
        im_AB = np.concatenate([im_A, im_B], 1)
        cv2.imwrite(path_AB, im_AB)    
