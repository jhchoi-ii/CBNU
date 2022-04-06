from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data1.csv', sep=",")



x = df[['temp','wind_speed','daylight_hour','humidity','Insolation','cloud']]
y = df[["value"]]
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size = 0.2)




#라쏘2
lasso2 = Lasso(alpha=10, max_iter=1000).fit(x_train, y_train)
y_predict2 = lasso2.predict(x_test)

print("훈련 세트의 정확도 : {:.2f}".format(lasso2.score(x_train, y_train)))
print("테스트 세트의 정확도 : {:.2f}".format(lasso2.score(x_test, y_test)))
print("Number of features used: {}".format(np.sum(lasso2.coef_ != 0)))

plt.figure(1)
plt.scatter(y_test, y_predict2, alpha=1)
plt.xlabel("Real Value")
plt.ylabel("Predicted Value")
plt.title("MULTIPLE LINEAR REGRESSION")


#라쏘3
lasso3 = Lasso(alpha=2000, max_iter=1000).fit(x_train, y_train)
y_predict3 = lasso3.predict(x_test)

print("훈련 세트의 정확도 : {:.2f}".format(lasso3.score(x_train, y_train)))
print("테스트 세트의 정확도 : {:.2f}".format(lasso3.score(x_test, y_test)))
print("Number of features used: {}".format(np.sum(lasso3.coef_ != 0)))


plt.scatter(y_test, y_predict3, alpha=0.4)
plt.xlabel("Real Value")
plt.ylabel("Predicted Value")
plt.title("MULTIPLE LINEAR REGRESSION")


#데이터간 연관 확인
#일사-발전량
plt.figure(2)
plt.title("Insolation")
plt.scatter(df[['Insolation']], df[['value']], alpha=0.4)
plt.show()

#일조-발전량
plt.figure(3)
plt.title("daylight_hour")
plt.scatter(df[['daylight_hour']], df[['value']], alpha=0.4)
plt.show()

#습도-발전량
plt.figure(4)
plt.title("Cloud")
plt.scatter(df[['cloud']], df[['value']], alpha=0.4)
plt.show()

#풍속-발전량
plt.figure(5)
plt.title("Wind speed")
plt.scatter(df[['wind_speed']], df[['value']], alpha=0.4)
plt.show()

#온도-발전량
plt.figure(6)
plt.title("Temp")
plt.scatter(df[['temp']], df[['value']], alpha=0.4)
plt.show()