#### 项目名称：一张图带你快速了解全球影视作品的数量情况

#### 项目简介：爬取豆瓣1万条影视数据，可视化分析不同分类的作品数量以及电影和电视的上映数量

#### 主要模块：scrapy、pymongo、numpy、pandas、matplotlib

#### 实现逻辑：

- ##### 构造链接：按下F12，查找与分析下载数据源的链接

- ##### 获取数据：使用Scrapy携带Cookies爬取站内全部影视数据

- ##### 清洗数据：标准的JSON格式数据，不需要清洗，直接下一步

- ##### 处理数据：对于某些不存在的字段，可以使用字典方法自动填充None

- ##### 保存数据：存储在MongoDB，获取的id字段赋值到_id特定字段，间接实现增量去重

- ##### 获取数据：使用pymongo连接MongoDB，附加额外数据源

- ##### 分析数据：若需要某些特定字符串，使用pandas和numpy的方法配合处理，再使用matplotlib制作可视化图表

- ##### 获得结论：

  - ##### 有37种分类，其中剧情类型的作品数量最多，接近喜剧类型的2倍

  - ##### 电视剧在1956年开始发展，可能人民逐渐有能力购买电视

  - ##### 电影和电视剧数量在1996年爆炸式增长，可能当时的政策推进，加之人民的生活水平不断提高和文化需求不断增多

- ##### 思考问题：

  - ##### 问：电视剧的数量会不会超过电影的？

  - ##### 答：现在AI智能时代，人民足不出户都能享受到电影的气氛，那么为了更好地享受电视剧的乐趣，应该可以照搬过去，直至超过。

##### 运行 dashboard_tv.py，显示以下图表：

![dashboard_tv](https://github.com/muzhouliu/data_spider/blob/master/dbtv/一张图/dashboard_tv.png)


##### 为了展示我的 Python 能力，附加额外数据源 (在 dump 文件夹) ，运行 dashboard_tvx.py，显示以下图表：

![dashboard_tvx](https://github.com/muzhouliu/data_spider/blob/master/dbtv/一张图/dashboard_tvx.png)
