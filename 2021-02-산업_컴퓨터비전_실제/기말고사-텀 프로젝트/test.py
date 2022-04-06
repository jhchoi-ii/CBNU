import cv2
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import argparse
import math

src1 = cv2.imread('b3 (6).jpg')
src2 = cv2.imread('b3 (7).jpg')

#src1 = cv2.imread('b0 (2).jpg')
#src2 = cv2.imread('b0 (8).jpg')

src2 = cv2.resize(src2, None, fx=0.5, fy=0.5)
src1 = cv2.resize(src1, None, fx=0.5, fy=0.5)

# 그레이스케일로 변환
gray1 = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)

# 코너점 찾는 함수, 그레이스케일 영상만 입력 가능
pt1 = cv2.goodFeaturesToTrack(gray1, 100, 0.01, 1)

# 찾은 코너점 정보를 옵티컬플로우 함수에 입력
# src1, src2에서 움직임 정보를 찾아내고 pt1에 입력한 좌표가 어디로 이동했는지 파악
pt2, status, err = cv2.calcOpticalFlowPyrLK(src1, src2, pt1, None)

# 가중합으로 개체가 어느 정도 이동했는지 보기 위함
dst = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)

_threshold = 30
moving = False
length = 0
# pt1과 pt2를 화면에 표시
for i in range(pt2.shape[0]):
    if status[i,0] == 0: # status = 0인 것은 제외, 잘못 찾은 것을 의미
        continue
        
    cv2.circle(dst, tuple(pt1[i, 0]), 4, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.circle(dst, tuple(pt2[i, 0]), 4, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.arrowedLine(dst, tuple(pt1[i, 0]), tuple(pt2[i, 0]), (0, 255, 0), 2)

    _pt = pt1[i, 0] - pt2[i, 0]
    _length = math.sqrt((_pt[0] * _pt[0]) + (_pt[1] * _pt[1]))

    if(length < _length):
        length = _length

if(length >= _threshold):
    moving = True

if(moving):
    print("Alarm")



cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()