# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 23:33:35 2021

@author: user
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import missingno as msno
import seaborn as sns

from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split

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

plt.figure(4)
plt.title("weekday-Distance")
plt.scatter(df[['weekday']], df[['Distance']], alpha=0.4)
plt.ylabel("Distance")
plt.xlabel("weekday")
plt.show()

plt.figure(5)
plt.title("humidity-Distance")
plt.scatter(df[['humidity']], df[['Distance']], alpha=0.4)
plt.ylabel("Distance")
plt.xlabel("humidity")
plt.show()


plt.figure(6)
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

plt.figure(7)
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

plt.figure(8)
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

plt.figure(9)
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

plt.figure(10)
plt.title("day")
# r-- : 짧은 실선, bs : 사각형, g% : 삼각형
plt.scatter(df[['id']], df[['Distance']] / 10000, color="black", alpha=0.4)
plt.scatter(df[['id']], df[['Count']] / 1000, color="orange", alpha=0.4)
plt.scatter(df[['id']], df[['minute']] / 100000, color="yellow", alpha=0.4)
plt.scatter(df[['id']], df[['weekday']], color="red", alpha=0.4)
plt.ylabel("Value")
plt.xlabel("ID")
plt.legend()
plt.show()

# Null 체크
msno.matrix(df=df.iloc[:,:], figsize=(8,8), color=(0.8, 0.5, 0.2))

# 분석 목표와 데이터 간의 관계확인, 예제용.
print( df[['weekday', 'Count']].groupby(['weekday'], as_index=True).count() )
print( df[['weekday', 'Distance']].groupby(['weekday'], as_index=True).count() )
print( df[['weekday', 'Count']].groupby(['weekday'], as_index=True).count() )

# 주말/공휴일에 따른 대여횟수/이용거리 분포
f, ax = plt.subplots(1, 1, figsize=(9, 5))
sns.kdeplot(df[df['weekday'] == 0]['Count'], ax=ax)
sns.kdeplot(df[df['weekday'] > 0]['Count'], ax=ax)
plt.legend(['weekday == 0', 'weekday == 1'])
plt.show()

f, ax = plt.subplots(1, 1, figsize=(9, 5))
sns.kdeplot(df[df['weekday'] == 0]['Distance'], ax=ax)
sns.kdeplot(df[df['weekday'] > 0]['Distance'], ax=ax)
plt.legend(['weekday == 0', 'weekday == 1'])
plt.show()

# 강우량에 따른 대여횟수/이용거리 분포
f, ax = plt.subplots(1, 1, figsize=(9, 5))
sns.kdeplot(df[df['rainfall'] == 0]['Count'], ax=ax)
sns.kdeplot(df[df['rainfall'] > 0]['Count'], ax=ax)
plt.legend(['rainfall == 0', 'rainfall == 1'])
plt.show()

f, ax = plt.subplots(1, 1, figsize=(9, 5))
sns.kdeplot(df[df['rainfall'] == 0]['Distance'], ax=ax)
sns.kdeplot(df[df['rainfall'] > 0]['Distance'], ax=ax)
plt.legend(['rainfall == 0', 'rainfall == 1'])
plt.show()

#데이터간 상관관계
cm =  df.corr()
print(cm)
    #히트맵
sns.heatmap(data=cm, annot=True)
plt.show()

colm = ['Count', 'Distance', 'avr-temp', 'rainfall', 'snow2', 'weekday']
sns.pairplot(df[colm])
plt.show()

#라쏘
x = df[['avr-temp', 'rainfall', 'snow1', 'snow2', 'weekday', 'humidity', 'sunshine']]
y = df[["Count"]]
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size = 0.2)

lasso = Lasso(alpha=0.1, max_iter=1000).fit(x_train, y_train)
y_predict = lasso.predict(x_test)

print("훈련 세트의 정확도 : {:.2f}".format(lasso.score(x_train, y_train)))
print("테스트 세트의 정확도 : {:.2f}".format(lasso.score(x_test, y_test)))
print("Number of features used: {}".format(np.sum(lasso.coef_ != 0)))

plt.figure(1)
plt.scatter(y_test, y_predict, alpha=0.5)
plt.xlabel("Real Value")
plt.ylabel("Predicted Value")
plt.title("Rasso")


