# encoding=utf-8
import pandas as pd
import numpy as np
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题

class CreatePng(object):
    def __init__(self):
        pass

    def create_Scatter(self,tables_name):
        df = pd.read_csv('./data_table/%s.csv' % tables_name, encoding='utf-8')
        # city_names = df['city_name'].values
        # for city in city_names:
        #     print(city)
        # 修改房价信息CSV再做图
        price = df[df.city_name == 'chongqing']['house_price_list'].values
        plt.scatter()
        plt.show()

    def create_histogram(self):
        # 各城市新房柱状图
        df = pd.read_csv('./data_table/count_city.csv',encoding='utf-8')
        y_house_num = df['house_num'].values
        x_city_name = df['city'].values

        for x, y in zip(x_city_name,y_house_num):
            plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
        plt.bar(x_city_name,y_house_num,facecolor='#9999ff',edgecolor='white')
        plt.show()


    def run(self):
        print('create scatter...')
        self.create_Scatter('house_price')
        # self.create_histogram()


if __name__ == '__main__':
    painter = CreatePng()
    painter.run()
