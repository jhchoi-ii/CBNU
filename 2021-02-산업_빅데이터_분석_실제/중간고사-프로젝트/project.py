# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 23:33:35 2021

@author: user
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', sep=",")
df["Distance"] = df["Distance"] / 1000
print(df)

#이동거리
distance = df["Distance"] / 1000

#대여횟수
count = df["Count"]

#대여시간
minute = df["minute"]

#일 최심신적설(cm) : 정해진 시간동안 쌓인 눈의 높이
snow1 = df["snow1"]
    
#일 최심적설 : 하루 중 가장 높이 쌓인 눈의 높이
snow2 = df["snow2"]

plt.figure(1)
plt.title("avr-temp-Distance")
plt.scatter(df[['avr-temp']], df[['Distance']], alpha=0.4)
plt.ylabel("Distance")
plt.xlabel("avr-temp")
plt.show()

plt.figure(2)
plt.title("rainfall-Distance")
plt.scatter(df[['rainfall']], df[['Distance']], alpha=0.4)
plt.ylabel("Distance")
plt.xlabel("rainfall")
plt.show()

plt.figure(3)
plt.title("Snow-Distance")
plt.scatter(df[['snow2']], df[['Distance']], alpha=0.4)
plt.ylabel("Distance")
plt.xlabel("snow")
plt.show()

plt.figure(7)
plt.title("weekday-Distance")
plt.scatter(df[['weekday']], df[['Distance']], alpha=0.4)
plt.ylabel("Distance")
plt.xlabel("weekday")
plt.show()

plt.figure(7)
plt.title("humidity-Distance")
plt.scatter(df[['humidity']], df[['Distance']], alpha=0.4)
plt.ylabel("Distance")
plt.xlabel("humidity")
plt.show()

plt.figure(4)
plt.title("Temp")
# r-- : 짧은 실선, bs : 사각형, g% : 삼각형
plt.scatter(df[['id']], df[['Distance']] / 10000, color="black", alpha=0.4)
plt.scatter(df[['id']], df[['Count']] / 1000, color="orange", alpha=0.4)
plt.scatter(df[['id']], df[['minute']] / 100000, color="yellow", alpha=0.4)
plt.scatter(df[['id']], df[['avr-temp']], color="red", alpha=0.4)
plt.ylabel("Value")
plt.xlabel("ID")
plt.legend()
plt.show()

plt.figure(5)
plt.title("Humidity")
# r-- : 짧은 실선, bs : 사각형, g% : 삼각형
plt.scatter(df[['id']], df[['Distance']] / 10000, color="black", alpha=0.4)
plt.scatter(df[['id']], df[['Count']] / 1000, color="orange", alpha=0.4)
plt.scatter(df[['id']], df[['minute']] / 100000, color="yellow", alpha=0.4)
plt.scatter(df[['id']], df[['humidity']], color="red", alpha=0.4)
plt.ylabel("Value")
plt.xlabel("ID")
plt.legend()
plt.show()

plt.figure(6)
plt.title("Sunshine")
# r-- : 짧은 실선, bs : 사각형, g% : 삼각형
plt.scatter(df[['id']], df[['Distance']] / 10000, color="black", alpha=0.4)
plt.scatter(df[['id']], df[['Count']] / 1000, color="orange", alpha=0.4)
plt.scatter(df[['id']], df[['minute']] / 100000, color="yellow", alpha=0.4)
plt.scatter(df[['id']], df[['sunshine']], color="red", alpha=0.4)
plt.ylabel("Value")
plt.xlabel("ID")
plt.legend()
plt.show()

plt.figure(6)
plt.title("rainfall")
# r-- : 짧은 실선, bs : 사각형, g% : 삼각형
plt.scatter(df[['id']], df[['Distance']] / 10000, color="black", alpha=0.4)
plt.scatter(df[['id']], df[['Count']] / 1000, color="orange", alpha=0.4)
plt.scatter(df[['id']], df[['minute']] / 100000, color="yellow", alpha=0.4)
plt.scatter(df[['id']], df[['rainfall']], color="red", alpha=0.4)
plt.ylabel("Value")
plt.xlabel("ID")
plt.legend()
plt.show()

