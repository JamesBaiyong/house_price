# encoding=utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class CreatePng(object):
    def __init__(self):
        pass

    def create_Scatter(self,tables_name):
        df = pd.read_csv('./data_table/%s.csv' % tables_name, encoding='utf-8')
        city_names = df['city_name'].values
        for city in city_names:
            print(city)
            price = df[df.city_name == city]['house_price_list'].values
            
            # plt.scatter()
            # plt.show()

    def create_histogram(self):
        pass

    def run(self):
        print('create scatter...')
        self.create_Scatter('house_price')


if __name__ == '__main__':
    painter = CreatePng()
    painter.run()
