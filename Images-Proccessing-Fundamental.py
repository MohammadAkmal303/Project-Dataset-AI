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

images1 = [cv2.imread(file1) for file1 in files1]
images2 = [cv2.imread(file2) for file2 in files2]

i = 1
for img1 in images1:
    img_adjusted1 = cv2.addWeighted(img1, 1.5, np.zeros(img1.shape, img1.dtype), 0, -12)
    img_name1 = "Dataset/img-procces-jeruknipis/" + str(i) + ".jpg"
    cv2.imwrite(img_name1, img_adjusted1)
    i += 1

x = 1
for img2 in images2:
    img_adjusted2 = cv2.addWeighted(img2, 1.5, np.zeros(img2.shape, img2.dtype), 0, 10)
    img_name2 = "Dataset/img-procces-Seledri/" + str(i) + ".jpg"
    cv2.imwrite(img_name2, img_adjusted2)
    x += 1
    