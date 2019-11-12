import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pymongo import MongoClient


# 全局中文
plt.rcParams['font.sans-serif'] = ['MicroSoft YaHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


client = MongoClient('127.0.0.1', 27017)
collection = client['dbtv']['tv']
tv = collection.find()

info_list = []
for info in tv:
	temp = {}
	temp['id'] = info['_id']
	temp['types'] = info['types']
	temp['subtype'] = info['subtype']
	temp['release_year'] = info['release_year']
	info_list.append(temp)

data = pd.DataFrame(info_list)
print(data.head())
print(data.info())


plt.figure(figsize=(16, 9), dpi=80)


# 离散字符串 + 构造数组
plt.subplot(121)

# 消除重复的分类
cate_list = list(set([c for i in data['types'] for c in i]))
print(len(cate_list))
# 根据原数组的行数、分类的长度、分类的名字，构造全为0的新数组
cate_zeros = pd.DataFrame(np.zeros((data.shape[0], len(cate_list))), columns=cate_list, dtype='int')

# 遍历分类列表，如果原数组字符串包含分类名字就赋1
data = data.astype({'types': np.str})
for m in cate_list:
	cate_zeros[m][data['types'].str.contains(m)] = 1
cate_count = cate_zeros.sum(axis=0).sort_values(ascending=True)

_x1 = cate_count.index
_y1 = cate_count.values
plt.barh(_x1, _y1)
plt.title('不同分类的影视作品数量统计')


# 时间序列 + 分组聚合
plt.subplot(122)

# 转化时间序列，设置时间索引
data['year'] = pd.to_datetime(data['release_year'])
data = data.set_index('year')

for subtype_name, subtype_data in data.groupby(by='subtype'):
	subtype_count = subtype_data.resample('Y')['id'].count()
	_x2 = [i.strftime('%Y') for i in subtype_count.index]
	_y2 = subtype_count.values
	plt.plot(_x2, _y2, label=subtype_name)

	if subtype_name == 'Movie':
		plt.xticks(_x2[::4], rotation=45)

	plt.title('电影和电视剧上映数量随时间的变化情况')
	plt.legend(loc='best')

plt.show()
