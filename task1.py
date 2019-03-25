'''
Requirments:
  python &
  > pip install pillow
  > pip install matplotlib
  > pip install numpy
Run:
  > python task1.py path/to/image
'''

import PIL
from PIL import Image
import numpy as np
import itertools
import sys
import os
import mylib
from mylib import BOX


# open image
image = Image.open(sys.argv[1]) # you have to pass the input image path as input arg
image = image.convert("L")  # convert to signle channeled image


outDir = sys.argv[2]

if not os.path.exists(outDir):
    os.makedirs(outDir)
width, height = image.size


totalPixels = width* height

freq = [0] * 256  # fill
cProbability = [0] * 256  # fill zeros



# save original image histogram
freq = image.histogram()


image.save(outDir+'/input.jpg')




centerX,centerY = (int(width/2),int(height/2))



# HISTOGRAM EQUALIZATION 
editableImage = image.load()
image = mylib.equalizeHistogram(image,editableImage,BOX(0,0,width,height)) # box of size image






# save resultant image and histogram
image.save(outDir+'/output.jpg')