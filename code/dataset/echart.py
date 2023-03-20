# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 22:49:54 2021

@author: kookil
"""
import datetime
import time
from pyecharts.charts import Bar,Line,Pie,Boxplot,Grid,HeatMap
from pyecharts import options as opts
import pandas as pd
import re
import numpy as np

def indexNumber(string):
    list = []
    actual =""
    # For each character of the string
    for i in range(len(string)):
        # If is number
        if"0" <= string[i] <="9":
            # Add number to actual list entry
            actual += string[i]
        # If not number and the list entry wasn't empty
        elif actual !="":
            list.append(actual);
            actual ="";
    # Check last entry
    if actual !="":
        list.append(actual);
    return list

excelFile = r'all.xls'
df = pd.DataFrame(pd.read_excel(excelFile))
singleprice=[]
price=df['价格'].tolist()
for i in price:
    money=indexNumber(str(i))
    if 0<len(money)<2:
        singleprice.append(int(money[0]))
    elif len(money)>=2:
        singleprice.append((int(money[0])+int(money[1]))/2)
    else:
        singleprice.append(-1)

# 1440751417.283 --> '2015-08-28 16:43:37.283'
def timestamp2string(timeStamp):
    try:
        d = datetime.datetime.fromtimestamp(timeStamp)
        str1 = d.strftime("%Y-%m-%d %H:%M:%S")
        # 2015-08-28 16:43:37.283000'
        return str1
    except Exception as e:
        print (e)
        return ''

df['intprice']=singleprice
begin = datetime.date(2021, 11, 27)
end = datetime.date(2022, 2, 28)

name=df['名称'].tolist()


artist=df['艺人'].tolist()


data=df['日期'].tolist()
datatimes=df.groupby(['日期']).sum()
d=df.groupby(['日期']).mean()
#x_data=datatimes.index.tolist()
#y_data=datatimes['演出状态'].tolist()
x_data=datatimes.index.tolist()
y_data=datatimes['演出状态'].tolist()
z_data=d['intprice'].tolist()

#df2=pd.DataFrame(pd.read_excel(r'dataact.xls'))
#y_data=df2['演出场次'].tolist()

#time=df['时间'].tolist()


#location=df['地点'].tolist()


#situation=df['演出状态'].tolist()
#s1 = df['演出状态'].value_counts()
#x_data=['0','1']
#y_data=[str(s1[0]),str(s1[1])]
#data_pair = [list(z) for z in zip(x_data, y_data)]
#x_data=[]
#y_data=[]

#localprice=df.groupby(['地点']).mean()
#x_data=localprice.index.tolist()
#y_data=localprice['intprice'].tolist()
##y_data=localprice['intprice'].tolist()
#
#localtime=df.groupby(['地点']).sum()
#z_data=localtime['演出状态'].tolist()
        
#pie=(
#        Pie()
#       .add("", data_pair)
#
#           .set_global_opts(title_opts=opts.TitleOpts(title=''), legend_opts=opts.LegendOpts(type_="scroll", pos_left="right", orient="vertical"))
#           .set_series_opts(label_opts=opts.LabelOpts(formatter="演出状态为{b}的有 {c}场", is_show=True))
#        )
#
#pie.render('演出状况.html')

bar = (
    Bar(init_opts=opts.InitOpts(width="1400px", height="700px")) # 设置图表大小
    .add_xaxis(xaxis_data=x_data)  # x轴
    .add_yaxis(
        series_name="日均演出(场)",  #柱形图系列名称
        yaxis_data=y_data, # 数据
        label_opts=opts.LabelOpts(is_show=True,position='top',formatter="{c}"), # 显示数据标签
        itemstyle_opts=opts.ItemStyleOpts(color="E16451",opacity=0.4),     # 柱形图颜色及透明度  
        )
    .extend_axis( # 设置次坐标轴
        yaxis=opts.AxisOpts(
            name="",  # 次坐标轴名称
            type_="value", # 次坐标手类型
            min_=0,  # 最小值
            max_=1000,  # 最大值
            is_show=True, # 是否显示
            axisline_opts=opts.AxisLineOpts(is_show=False,# y轴线不显示
                                           linestyle_opts=opts.LineStyleOpts(color='99B9FF')), # 设置线颜色, 字体颜色也变
            axistick_opts=opts.AxisTickOpts(is_show=False),   # 刻度线不显示
            axislabel_opts=opts.LabelOpts(formatter="{value}"), # 次坐标轴数据显示格式
                            )
                )  
    .set_global_opts(title_opts=opts.TitleOpts(title="日演出情况",# 标题
                                               title_textstyle_opts=opts.TextStyleOpts(font_size=20), #主标题字体大小
                                               subtitle="日演出次数与日均价", # 次坐标轴
                                               pos_left='6%'),# 标题位置
                     legend_opts=opts.LegendOpts(is_show=False),  # 不显示图例
                     tooltip_opts=opts.TooltipOpts(trigger="axis"),# 提示框
                     yaxis_opts=opts.AxisOpts(type_="value", # y轴类型
                                              name='单位: 场', # y轴名称
                                              name_location='middle', # y轴名称位置
                                              name_gap=50,  # y轴名称距离轴线距离
                                              axistick_opts=opts.AxisTickOpts(is_show=False),   # 刻度线
                                              axisline_opts=opts.AxisLineOpts(is_show=False),   # y轴线
                                              splitline_opts=opts.SplitLineOpts(is_show=True),   # y轴网格线
                                              axislabel_opts=opts.LabelOpts(formatter="{value}")), # 轴标签显示方式
                      )   
    )

line = (
    Line()
    .add_xaxis(xaxis_data=x_data) # x轴
    .add_yaxis(
        series_name="日演出均价",  # 名称
        yaxis_index=1,  # 次坐标z_data
        is_smooth=True,# 线条样式  , 是否设置成圆滑曲线
        y_axis=z_data,
        itemstyle_opts=opts.ItemStyleOpts(color="#f6c065"),     # 标记的颜色
        linestyle_opts=opts.LineStyleOpts(width=3,color ='#f6c065'), # 线条颜色和宽度
        )
    )


bar.overlap(line) # 图表组合
bar.render("演出场地情况.html")

#def heatmap_car() -> HeatMap:
#    x = ['周六', '周日','周一', '周二', '周三', '周四', '周五']
#    y = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17']
#    value = [[i, j, z]
#         for i in range(len(x)) for j in range(len(y)) for z in y_data]
#    c = (
#        HeatMap()
#        .add_xaxis(x)
#        .add_yaxis("演出", y, value)
#        .set_global_opts(
#            title_opts=opts.TitleOpts(title="日演出热力图(11.27-3.4)"),
#            visualmap_opts=opts.VisualMapOpts(),
#        )
#    )
#    return c
#
#heatmap_car().render('日演出热力图.html')
#list=[]
#x = ['周六', '周日','周一', '周二', '周三', '周四', '周五']
#y = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17']
#z = y_data
#for i in range(len(x)):
#    for j in range(len(y)):
#        for k in z:
#            l=[i,j,k]
#            list.append(l)
#heat=(
#      HeatMap()
#      .add_xaxis(x)
#      .add_yaxis(
#             "演出数量/场" ,
#             y,z)
#      .set_global_opts(
#            title_opts=opts.TitleOpts(title="每日演出数量"),
#            visualmap_opts=opts.VisualMapOpts(),
#        ))
#heat.render("日演出热力图.html")