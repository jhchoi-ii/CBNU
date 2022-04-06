import cv2
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import argparse
import math

src1 = cv2.imread('b3 (6).jpg')
src2 = cv2.imread('b3 (7).jpg')

src1 = cv2.imread('b0 (2).jpg')
src2 = cv2.imread('b0 (8).jpg')

src2 = cv2.resize(src2, None, fx=0.5, fy=0.5)
src1 = cv2.resize(src1, None, fx=0.5, fy=0.5)

gray1 = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)

pt1 = cv2.goodFeaturesToTrack(gray1, 100, 0.01, 1)

pt2, status, err = cv2.calcOpticalFlowPyrLK(src1, src2, pt1, None)

dst = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)

_threshold = 30
moving = False
length = 0
for i in range(pt2.shape[0]):
    if status[i,0] == 0:
        continue
        
    cv2.circle(dst, tuple(pt1[i, 0]), 4, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.circle(dst, tuple(pt2[i, 0]), 4, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.arrowedLine(dst, tuple(pt1[i, 0]), tuple(pt2[i, 0]), (0, 255, 0), 2)

    _pt = pt1[i, 0] - pt2[i, 0]
    _length = math.sqrt((_pt[0] * _pt[0]) + (_pt[1] * _pt[1]))

    if(length < _length):
        length = _length

if(length < _threshold):
    moving = True

if(moving):
    print("Alarm")

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()