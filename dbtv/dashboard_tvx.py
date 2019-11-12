import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pymongo import MongoClient


# 全局中文
plt.rcParams['font.sans-serif'] = ['MicroSoft YaHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


client = MongoClient('127.0.0.1', 27017)
collection = client['dbtv']['tvx']
tvx = collection.find()

info_list = []
for info in tvx:
	temp = {}
	temp['info'] = info['info']
	temp['rate'] = info['rating']['value']
	temp['title'] = info['title']
	temp['country'] = info['tv_category']
	temp['directors'] = info['directors']
	temp['actors'] = info['actors']
	info_list.append(temp)

data = pd.DataFrame(info_list)
print(data.head())
print(data.info())


plt.figure(figsize=(16, 9), dpi=120)


# 图1: 简单分组聚合
plt.subplot(221)
country_group = data.groupby(by='country')
rate_avg = country_group['rate'].mean()

_x1 = rate_avg.index
_y1 = rate_avg.values
plt.bar(_x1, _y1, width=0.5)
plt.yticks(range(11))
plt.title('各个国家的电视剧平均评分统计')


# 图2: 离散字符串 + 构造数组
plt.subplot(222)

# 合并导演和演员的名字
for n in range(data.shape[0]):
	data['directors'][n].extend(data['actors'][n])

# 删除包含导演和演员的名字的元素
temp_list = data['info'].str.split('/')
for c in range(data.shape[0]):
	for p in range(len(data.loc[c,'directors'])):
		temp_list.loc[c].pop(0)  # 删除p次列表的第一个

# 消除重复值，只要字符长度小于等于2的类型
cate_list = list(set([c for i in temp_list for c in i[:-1] if len(c)<3]))

# 根据原数组的行数、分类的长度、分类的名字，构造全为0的数组
cate_zeros = pd.DataFrame(np.zeros((data.shape[0], len(cate_list))), columns=cate_list, dtype='int')

# 遍历分类列表，如果原数组字符串包含分类名字就赋1
for m in cate_list:
	cate_zeros[m][data['info'].str.contains(m)] = 1
cate_count = cate_zeros.sum(axis=0).sort_values(ascending=True)

_x2 = cate_count.index
_y2 = cate_count.values
plt.barh(_x2, _y2)
plt.title('不同分类的电视剧数量统计')


# 图3: 简单时间序列
plt.subplot(223)

# 重新分裂，只要（2019-10）7个字符的，其他为nan
temp_list = data['info'].str.split('/').tolist()
datetime_list = [i[-1].rsplit('-', 1)[0] if len(i[-1].rsplit('-', 1)[0]) == 7 else np.nan for i in temp_list]

# 在原数组添加列，转化时间序列
data['datetime'] = pd.DataFrame(np.array(datetime_list).reshape((data.shape[0], 1)))
data['datetime'] = pd.to_datetime(data['datetime'])

# 预处理全部数据再定位数据，选取大于7分的数据和删除有nan的行
data = data[data['rate'] > 7].copy()  # 添加copy，避免SettingWithCopyWarning
data = data.dropna(axis=0, how='any')  # 不要这行也可以，count时自动跳过nan

# 设置时间序列索引，降采样
data = data.set_index('datetime')
tv_count = data.resample('6M')['title'].count()

_x3 = [i.strftime('%Y-%m') for i in tv_count.index]
_y3 = tv_count.values

plt.scatter(_x3, _y3, s=10)
plt.xticks(_x3[::4], rotation=45)
plt.title('7分以上电视剧时长随时间的分布情况')


# 图4: 时间序列 + 分组聚合
plt.subplot(224)

# 不同国家分组聚合
for c_name, c_data in data.groupby(by='country'):
	c_count = c_data.resample('6M')['info'].count()

	_x4 = [i.strftime('%Y-%m') for i in c_count.index]
	_y4 = c_count.values

	plt.plot(range(len(_x4)), _y4, label=c_name)

	# 因为数据源不完整，部分数据缺失，使用x最长的为横坐标
	if c_name == 'american':
		plt.xticks(range(len(_x4))[::4], _x4[::4], rotation=45)

	plt.title('不同国家的7分以上电视剧随时间的变化情况')
	plt.legend(loc='best')

plt.show()
