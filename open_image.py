# !/home/atif/myenv/bin/python

import cv2
import matplotlib.pyplot as plt
from img_process import do_gray

dir = "/media/atif/BE0E05910E0543BD/University of Bremen MSc/git_submodule/open_image/"
path = dir+"photo.jpg"

import os
print(os.getcwd())

# path = 'photo.jpg'
frame = cv2.imread(path)
# hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# cv2.imwrite(dir+'cv2_image.png',img_gray)

# print(frame)

# def do_gray(file):
#     img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     return img_gray

gray_img = do_gray(frame)

cv2.imwrite(dir+'cv2_image.png', gray_img)
cv2.imshow('RGB', frame)
# cv2.imshow('GRAY', gray_img)
if cv2.waitKey() == ord('q'):
    cv2.destroyAllWindows()