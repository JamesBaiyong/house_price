#encoding=utf-8
import pandas as pd
import csv
import re
import sys
import numpy
import json
from collections import defaultdict
reload(sys)
sys.setdefaultencoding('utf-8')


province = {
    'zhongshan':'中山',
    'chongqing':'重庆',
    'changsha':'长沙',
    'chengdu':'成都',
    'dalian':'大连',
    'hangzhou':'杭州',
    'kunming':'昆明',
    'nanjing':'南京',
    'suzhou':'苏州',
    'tianjin':'天津',
    'wuhan':'武汉',
    'xian':'西安'
}

class ClearMoney(object):
    def __init__(self):
        self.csv_file = open('./data_table/house_price.csv','w')
        self.writers = csv.writer(self.csv_file)
        self.writers.writerow(['city_name','mean','variance','median'])
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

    def run(self):
        for city_name in self.tables:
            self.clear(city_name)
        # self.clear("chongqing")
        self.csv_file.close()

    def clear(self,city_name):
        df = pd.read_csv('./data_table/%s.csv' % city_name, encoding='utf-8')
        # 房屋面积
        house_area = df.area.values
        # 提取出房价列
        house_price = df.price.values
        # 提取出房类型
        house_type = df.type
        # 提取地方
        house_addres = df.position
        # 楼盘名
        house_name = df.name.values
        house_price_list = self.extract_money(house_price)
        #　房价平均值
        mean = sum(house_price_list) / len(house_price_list)
        # 房价方差
        variance = self.get_variance(house_price_list)
        # 房价中位数
        median = self.get_median(house_price_list)
        # 写入房价相关数据
        try:
            self.writers.writerow([province[city_name],mean,variance,median])
        except:
            self.csv_file.close()
        # house_price_area = self.extract_money_area(city_name,house_price,house_area)


    def extract_money(self,house_price):
        # 清洗房价的格式,去除影响房价信息
        money_list = []
        # money_dict = defaultdict(list)
        house_info = len(house_price)
        for item in range(house_info):
            money_com = re.compile('(\d+)')
            try:
                money = int(re.match(money_com,house_price[item]).group(1))
                if money <= 2000:
                    continue
                money_list.append(money)
            except:
                pass
        return money_list
        # money_json = json.dumps(money_dict, ensure_ascii = False, indent = 4)
        # return money_json

    def extract_money_area(self,city_name,house_price,house_area):
        csv_file = open('./data_table/house_price/house_price_%s.csv'%city_name,'w')
        writers = csv.writer(csv_file)
        writers.writerow(['house_price','house_price'])
        house_info = len(house_price)
        area_list = []
        for item in range(house_info):
            money_com = re.compile('(\d+)')
            try:
                area = re.findall(money_com, house_area[item])[0]
            except:
                area = 100
            try:
                money = int(re.match(money_com,house_price[item]).group(1))
                if money <= 2000:
                    continue
            except:
                continue
                # money_list.append(money)
                # area_list.append(area)
            writers.writerow([money,area])
        csv_file.close()
        return area_list

    def extract_address(self):
        pass

    # 　房价中位数
    def get_median(self,data):
        data = sorted(data)
        size = len(data)
        if size % 2 == 0:  # 判断列表长度为偶数
            median = (data[size // 2] + data[size // 2 - 1]) / 2
            data[0] = median
        if size % 2 == 1:  # 判断列表长度为奇数
            median = data[(size - 1) // 2]
            data[0] = median
        return data[0]

    def get_variance(self,data):
        N = len(data)
        narray = numpy.array(data)
        sum1 = narray.sum()
        narray2 = narray * narray
        sum2 = narray2.sum()
        mean = sum1 / N
        var = sum2 / N - mean ** 2
        return var

if __name__ == '__main__':
    worker = ClearMoney()
    worker.run()
