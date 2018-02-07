# encoding=utf-8
import pandas as pd

# tables = [
#     'zhongshan',
#     'chongqing',
#     'changsha',
#     'chengdu',
#     'dalian',
#     'hangzhou',
#     'kunming',
#     'nanjing',
#     'tianjin',
#     'wuhan',
#     'xian']
# 例子例子大例子

# 对销售状态做去重,查看有多少种销售状态
# for i in tables:
#     df = pd.read_csv('./data_table/%s.csv'%i,encoding='utf-8')
#     state_num = df.drop_duplicates(['state'])['state']
#     print(state_num)

# 对房屋类型去重
# for i in tables:
#     df = pd.read_csv('./data_table/%s.csv' % i, encoding='utf-8')
#     type_num = df.drop_duplicates(['type'])['type']  # 对指定列去重
#     print(type_num)

# 计数
# print len(df[df.type == "住宅"])

# df = pd.read_csv('./data_table/count_city.csv',encoding='utf-8')
# print df

import numpy as np
import matplotlib.pyplot as plt

N = 5
men_means = (20, 35, 30, 35, 27)
men_std = (2, 3, 4, 1, 2)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, men_means, width, color='r', yerr=men_std)

women_means = (25, 32, 34, 20, 25)
women_std = (3, 5, 2, 3, 3)
rects2 = ax.bar(ind + width, women_means, width, color='y', yerr=women_std)

# add some text for labels, title and axes ticks
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))

ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()