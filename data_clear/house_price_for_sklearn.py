#encoding=utf-8
import csv
import re
import sys
import pandas as pd
reload(sys)
sys.setdefaultencoding('utf-8')

class CreateHouseForSklearn(object):
    def __init__(self):
        pass

    def create_house_price(self):
        df = pd.read_csv('./data_table/chongqing.csv', encoding='utf-8')
        house_price = df['price'].values
        house_area = df['area'].values
        self.house_name = df['name'].values
        self.house_loaction = df['position'].values
        self.house_type = df['type'].values
        self.extract_money_area(house_price,house_area)
        # 总计
    def extract_money_area(self,house_price,house_area):
        csv_file = open('./data_table/chongqing_house.csv','w')
        writers = csv.writer(csv_file)
        writers.writerow(['CompanyPrice','area','price','name','location','type'])
        house_info = len(house_price)
        area_list = []
        for item in range(house_info):
            money_com = re.compile('(\d+)')
            loaction_compile = re.compile('(.*?)-')
            try:
                area = int(re.findall(money_com, house_area[item])[0])
            except:
                continue
            try:
                money = int(re.match(money_com,house_price[item]).group(1))
                if money <= 2000:
                    continue
            except:
                continue
            #　预估成交价
            price = (money * area)
            house_type =  self.house_type[item]
            house_name = self.house_name[item]
            location = re.findall(loaction_compile,self.house_loaction[item])[0]

            writers.writerow([money,area,price,house_name,location,house_type])
        csv_file.close()
        return area_list

    def run(self):
        self.create_house_price()

if __name__ == '__main__':
    worker = CreateHouseForSklearn()
    worker.run()
