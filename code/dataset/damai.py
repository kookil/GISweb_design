# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 13:46:22 2021

@author: kookil
"""
from selenium import webdriver
import time
import warnings
warnings.filterwarnings("ignore")
#大麦网爬虫

f = open("damai.csv", 'w', encoding='utf-8')
ls = ['名称', '艺人', '价格', '时间', '地点']
f.write(",".join(ls)+"\n")
#提示中的代码
fp = webdriver.FirefoxProfile()
# 限制CSS加载
fp.set_preference("permissions.default.stylesheet", 2)
# 限制图片加载
fp.set_preference('permissions.default.image', 2)
# 限制JavaScript执行
fp.set_preference('javascript.enabled', False)

driver = webdriver.Firefox(executable_path = r'geckodriver.exe',firefox_profile=fp)
driver.implicitly_wait(3)#隐式等待1s
driver.get("https://search.damai.cn/search.htm?spm=a2oeg.home.card_0.dviewall.591b23e11ImhAf&ctl=%E6%BC%94%E5%94%B1%E4%BC%9A&order=1&cty=%E4%B8%8A%E6%B5%B7")
for i in range(2):
    time.sleep(3)
    try:
        main = driver.find_element_by_class_name("search-box")
        tickets = main.find_element_by_class_name("item__box")
    
        tickets_list = tickets.find_elements_by_class_name("items")
    
        for m in tickets_list:
            ticket = []
            # print(m.get_attribute("innerHTML"))
            ma = m.find_element_by_class_name("items__txt")
            name = ma.find_element_by_class_name("items__txt__title")
            name1 = name.find_element_by_tag_name("a").get_attribute("innerHTML")
    
            time_list = ma.find_elements_by_class_name("items__txt__time")
            lengh = len(time_list)
            print(lengh)
            n = [" ", " ", "艺人：无介绍"]
            for j in range(lengh):
                k = lengh - j - 1
                n[j] = time_list[k].text
                # print(n[i].get_attribute("innerHTML"))
    
            performers = n[2]
            place = n[1][0:2]+n[1][5:len(n[1])+1]
            times = n[0]
    
            price = ma.find_element_by_class_name("items__txt__price")
            price1 = price.find_element_by_tag_name('span').text
  
            ticket.append(name1)
            ticket.append(performers)
            ticket.append(price1)
            ticket.append(times)
            ticket.append(place)
    
            # print(ticket)
            f.write(",".join(ticket)+"\n")
            print("完成")
    
        pagenext = driver.find_element_by_class_name('btn-next')
        pagenext.click()
        time.sleep(3)
        nextpage=main.find_element_by_class_name("sort_next")
        nextpage.click()
    
    except Exception as err:
        print("未爬取成功：", err)


print("结束")
f.close()
driver.quit()
