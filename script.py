import numpy as np
import cv2
import glob

img_dir1 = "Dataset/jeruknipis/"
img_dir2 = "Dataset/Seledri/"

ext = ['jpg', 'png']

files1 = []
files2 = []

[files1.extend(glob.glob(img_dir1 + '*.' + e)) for e in ext]
[files2.extend(glob.glob(img_dir2 + '*.' + e)) for e in ext]