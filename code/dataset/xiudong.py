# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 20:15:57 2021

@author: kookil
"""

from selenium import webdriver
import time

f = open("xiudong.csv", 'w', encoding='utf-8')
ls = ['名称', '艺人', '价格', '时间', '地点']
f.write(",".join(ls)+"\n")

fp = webdriver.FirefoxProfile()
# 限制CSS加载
fp.set_preference("permissions.default.stylesheet", 2)
# 限制图片加载
fp.set_preference('permissions.default.image', 2)
# 限制JavaScript执行
fp.set_preference('javascript.enabled', False)

driver = webdriver.Firefox(executable_path = r'geckodriver.exe',firefox_profile=fp)
driver.implicitly_wait(3)#隐式等待1s

for page in range(21):#逐页爬取
    if page == 1:
        driver.get("https://www.showstart.com/event/list?pageNo=1&pageSize=20&cityCode=21&sortType=9")
    else:
        driver.get("https://www.showstart.com/event/list?pageNo="+str(page+1)+"&pageSize=20&cityCode=21&sortType=9")

    try:
        main = driver.find_element_by_class_name("el-main")
        tic = main.find_element_by_class_name("show-list.layout")
        tickets = main.find_element_by_class_name("list-box.clearfix")
        tickets_list = tickets.find_elements_by_tag_name("a")
        # print(tickets_list)
        for m in tickets_list:
            ticket = []
            name = m.find_element_by_class_name("title").text
            performers = m.find_element_by_class_name("artist").text
            price = m.find_element_by_class_name("price").text[3:]
            times = m.find_element_by_class_name("time").text[3:]
            place = "上海"+m.find_element_by_class_name("addr").text[4:]

            ticket.append(name)
            ticket.append(performers)
            ticket.append(price)
            ticket.append(times)
            ticket.append(place)

            # print(ticket)
            f.write(",".join(ticket) + "\n")
            print("完成")

    except Exception as err:
        print("未爬取成功：", err)

    time.sleep(3)

print("结束")
f.close()
driver.quit()
