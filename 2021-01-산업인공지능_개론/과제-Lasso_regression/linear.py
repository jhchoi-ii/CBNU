from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data1.csv', sep=",")
x = df[['temp','wind_speed','daylight_hour','Insolation','cloud']]
y = df[["value"]]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.9, test_size = 0.1)

line_fitter = LinearRegression()
line_fitter.fit(x_train, y_train)

y_predict = line_fitter.predict(x_test)

plt.scatter(y_test, y_predict, alpha=0.4)
plt.xlabel("Real Value")
plt.ylabel("Predicted Value")
plt.title("MULTIPLE LINEAR REGRESSION")
plt.show()

print("훈련 세트의 정확도 : {:.2f}".format(line_fitter.score(x_train, y_train)))
print("테스트 세트의 정확도 : {:.2f}".format(line_fitter.score(x_test, y_test)))