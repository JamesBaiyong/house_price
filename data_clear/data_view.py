# encoding=utf-8
import pandas as pd
import numpy as np
from matplotlib.font_manager import FontProperties
from pylab import *

mpl.rcParams[u'font.sans-serif'] = ['simhei']
# mpl.rcParams['font.sans-serif'] = ['simhei'] #指定默认字体
# mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题

class CreatePng(object):
    def __init__(self):
        self.tables = [
            'zhongshan',
            'chongqing',
            'changsha',
            'chengdu',
            'dalian',
            'hangzhou',
            'kunming',
            'nanjing',
            'tianjin',
            'wuhan',
            'xian']

    def create_Scatter(self,tables_name):
        df = pd.read_csv('./data_table/house_price/house_price_%s.csv' % tables_name, encoding='utf-8')
        # city_names = df['city_name'].values
        # for city in city_names:
        #     print(city)
        # 修改房价信息CSV再做图
        price = df['house_price'].values
        plt.scatter(price,np.arange(len(price)))
        plt.savefig('./picture/%s_scatter.png'%tables_name)
        plt.close()
        return None

    def create_histogram_new_house(self):
        # 各城市新房柱状图
        df = pd.read_csv('./data_table/count_city.csv',encoding='utf-8')
        y_house_num = df['house_num'].values
        x_city_name = df['city'].values

        for x, y in zip(x_city_name,y_house_num):
            plt.text(x, y, '%.2f' % y, ha='center', va='bottom')
        plt.bar(x_city_name,y_house_num,facecolor='#9999ff',edgecolor='white')
        plt.show()

    def create_histogram_type(self):
        #　各城市新房类型
        n_groups = 11
        index = np.arange(n_groups)
        total_width, n = 0.8, 3
        width = total_width / n
        index = index - (total_width - width) / 2
        fig, ax = plt.subplots()
        df = pd.read_csv('./data_table/count_city_table.csv',encoding='utf-8')
        city = df['city'].values
        business = df['business'].values
        residence = df['residence'].values
        villa = df['villa'].values

        def autolabel(rects):
            """
            在每个柱上标数字
            """
            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width() / 2., 1 * height,
                        '%d' % int(height),
                        ha='center', va='bottom')

        rects1 = plt.bar(index,business,width,alpha=0.4,color='b',label=u'商业类')
        rects2 = plt.bar(index+width,residence,width,alpha=0.4,color='g',label=u'住宅类')
        rects3 = plt.bar(index+2*width,villa,width,alpha=0.4,color='r',label=u'别墅类')

        autolabel(rects1)
        autolabel(rects2)
        autolabel(rects3)
        plt.xticks(index + width, city)
        plt.yticks(fontsize=18)  # change the num axis size
        plt.legend()
        plt.tight_layout()
        plt.show()

    def create_ze_house(self):
        df = pd.read_csv('./data_table/house_price.csv',encoding='utf-8')
        city = df.city_name.values
        print city
        mean = df['mean'].values
        variance = df.variance.values
        median = df['median'].values
        x = range(len(city))
        plt.plot(x, mean, 'ro-',label=u'平均值')
        plt.plot(x,median,'g--',label=u'中位数')
        plt.xticks(x, city)
        plt.legend()
        plt.show()


    def run(self):
        # for table in self.tables:
        #     self.create_Scatter(table)
        #     print table
        self.create_ze_house()
        # self.create_histogram_new_house()
        # self.create_histogram_type()
        # self.drawBarChartPoseRatio()


if __name__ == '__main__':
    painter = CreatePng()
    painter.run()
