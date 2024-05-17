import numpy as np
import cv2 as cv
import argparse
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("--image_path", help = "Enter the path of your image")
parser.add_argument("--output_path", help = "name of output path")
args = vars(parser.parse_args())

img = cv.imread(args['image_path'])
#cv.imwrite("output_dir,img)
assert img is not None, "file could not be read, check with os.path.exists()"
color = ('b','g','r')
for i,col in enumerate(color):
 histr = cv.calcHist([img],[i],None,[256],[0,256])
 plt.plot(histr,color = col)
 plt.xlim([0,256])
plt.show()