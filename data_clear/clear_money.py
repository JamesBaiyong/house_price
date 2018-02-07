#encoding=utf-8
import pandas as pd
import csv
import re
import sys
import json
from collections import defaultdict
reload(sys)
sys.setdefaultencoding('utf-8')

class ClearMoney(object):
    def __init__(self):
        self.csv_file = open('./data_table/house_price.csv','w')
        self.writers = csv.writer(self.csv_file)
        self.writers.writerow(['city_name', 'house_price_list','mean'])
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
        mean = sum(house_price_list) / len(house_price_list)

        try:
            self.writers.writerow([city_name,house_price_list,mean])
        except:
            self.csv_file.close()
        house_price_area = self.extract_money_area(city_name,house_price,house_area)


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

if __name__ == '__main__':
    worker = ClearMoney()
    worker.run()
