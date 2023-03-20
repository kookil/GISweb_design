#!/usr/bin/python3

from pyecharts.charts import Bar,Pie   # 注意，新版本中，Pie被放进了charts
from pyecharts import options as opts
#from config.settings import MYSQL_HOST,MYSQL_PORT,MYSQL_USER,MYSQL_PASSWD,MYSQL_DB

import pymysql

# 查询所有字段
def list_col(localhost, username, pd, db, tabls_name):
    try:
        db = pymysql.connect(host=localhost, user=username, password=pd,  database=db, charset="utf8")
        cursor = db.cursor()
        cursor.execute("select * from %s" % tabls_name)
        col_name_list = [tuple[0] for tuple in cursor.description]
        db.close()
        return col_name_list
    except pymysql.Error as e:
        print("数据库连接失败："+str(e))

# 列出所有的表
def list_table(localhost, username, pd, db):
    try:
        db = pymysql.connect(host=localhost, user=username, password=pd,  database=db, charset="utf8")
        cursor = db.cursor()
        cursor.execute("show tables")
        table_list = [tuple[0] for tuple in cursor.fetchall()]
        db.close()
        return table_list
    except pymysql.Error as e:
        print("数据库连接失败："+str(e))


username = "root" # 用户名
password = "Gyj001202" # 连接密码
localhost = "localhost" # 连接地址
database = "act" # 数据库名
tables = list_table(localhost, username, password, database) # 获取所有表，返回的是一个可迭代对象
print(tables) 

for table in tables:
    col_names = list_col(localhost, username, password, database, table)
    print(col_names) # 输出所有字段名


## 数据可视化
#from pyecharts.globals import ThemeType         # 内置主题类型
#
## 柱状图
#bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.MACARONS))
## x为发布日期，y为客运量 间隔
#bar.add_xaxis(namelist)
#bar.add_yaxis("数量", numlist, category_gap="50%")
## 基本设置
#bar.set_global_opts(title_opts=opts.TitleOpts(title="时间范围分布图"),
#                    yaxis_opts=opts.AxisOpts(name="单日演出数量(单位:场)"),  # 设置y轴名字，x轴同理
#                    xaxis_opts=opts.AxisOpts(name="时间范围"),
#                    datazoom_opts=opts.DataZoomOpts()  # 设置水平缩放，默认可滑动(*好东西)
#                    )
## 标记峰值
#bar.set_series_opts(
#    label_opts=opts.LabelOpts(is_show=True),
#    markpoint_opts=opts.MarkPointOpts(
#        data=[
#            opts.MarkPointItem(type_='max', name='最大值'),  # 最大值标记点
#            opts.MarkPointItem(type_='min', name='最小值'),  # 最小值标记点
#            opts.MarkPointItem(type_='average', name='平均值')  # 平均值标记点
#        ]
#    )
#)
#
#bar.render('时间范围分布图.html')  # 输出为html







