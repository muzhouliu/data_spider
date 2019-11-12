##### 项目名称：四张图带你快速了解网易CC直播的运营情况

##### 项目简介：三天累计爬取123万条直播数据，可视化分析站内访问量、游戏热度以及主播画像、增长率、活跃人数和地区分布 

##### 主要工具：Python、MySQL、MongoDB、Tableau

##### 实现逻辑：

- ##### 构造链接：按下F12，查找与分析下载数据源的链接

- ##### 获取数据：使用Scrapy每5分钟定时爬取站内最新直播数据 

- ##### 清洗数据：标准的JSON格式数据，不需要清洗，直接下一步 

- ##### 处理数据：对于某些不存在的字段，可以使用字典方法自动填充None

- ##### 保存数据：同时存储在MySQL和MongoDB（备份作用，间接实现增量去重）

- #####  分析数据：使用Tableau连接MySQL，混合中国行政区划代码数据源，高效制作图表

- #####  获得结论：

  - ##### 站内平均访问量560K

  - ##### 梦幻西游电脑版和星秀总和热度最高

  - ##### 18~29岁的男性主播居多

  - ##### 2018年主播数量同比增长451.1% 

  - ##### 大部分主播分布在广州市、成都市和杭州市

- ##### 思考问题：

  - ##### 问：为什么主要运营7类游戏，而不砸钱吸纳更多人，快速扩大规模？

  - ##### 答：也许网易CC直播是一款公益平台，主要功能为绿色无广告、优质语音、兑换道具商品以及游戏全记录。


![仪表板1](https://github.com/muzhouliu/data_spider/blob/master/necc/四张图/仪表板%201.png)

![仪表板2](https://github.com/muzhouliu/data_spider/blob/master/necc/四张图/仪表板%202.png)

![仪表板3](https://github.com/muzhouliu/data_spider/blob/master/necc/四张图/仪表板%203.png)

![仪表板4](https://github.com/muzhouliu/data_spider/blob/master/necc/四张图/仪表板%204.png)


##### 数据源下载地址：

##### *链接: https://pan.baidu.com/s/1TInWjQzw1RcqBFkbLKhmew 提取码: 6h56*
