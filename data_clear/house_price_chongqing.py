#encoding=utf-8
# 线性回归+房价与房屋尺寸关系的线性拟合
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model

datasets_X = []
datasets_Y = []

df = pd.read_csv('/home/baiyong/my_code/house_price/data_clear/data_table/chongqing_house.csv')
df_house = df[df.type == "住宅"] # 筛选住宅
datasets_Y = df_house['price'].values
datasets_X = df_house['area'].values


length = len(datasets_X)
print type(datasets_X)

datasets_X = np.array(datasets_X).reshape([length,1])
datasets_Y = np.array(datasets_Y)

minX = min(datasets_X)
maxX = max(datasets_X)
X = np.arange(minX,maxX).reshape([-1,1]) # 以数据datasets_X的最大值和最小值为范围,建立等差数列,方便后续画图。
linear = linear_model.LinearRegression()
linear.fit(datasets_X,datasets_Y)

plt.scatter(datasets_X, datasets_Y, color = 'red',alpha=0.5)
plt.plot(X, linear.predict(X), color = 'blue',alpha=0.5)
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()
