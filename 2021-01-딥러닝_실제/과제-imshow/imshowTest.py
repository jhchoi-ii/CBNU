# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('pic.png')

plt.imshow(img)
plt.show()