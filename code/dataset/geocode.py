# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 00:08:15 2021

@author: kookil
"""
import json
import pandas as pd
import requests
service ="http://api.map.baidu.com/geocoding/v3/?"#正向
service1 ="http://api.map.baidu.com/reverse_geocoding/v3/?"#逆向
output = "json"
AK= "4x8VltXZwiZgfvXZCgwnnATIGPZhZwVM" 
pois = 1
zoom = 10
df = pd.read_excel("all.xls")
df1 = pd.read_excel("all.xls")['地点'].tolist()
l_lng=[]
l_lat=[]
for address in df1:
    parameters = f"address={address}&output={output}&ak={AK}"
    url = service + parameters
    response = requests.get(url)
    text=response.text
    dic=json.loads(text)
    status = dic["status"]
    if status==0:
        lng = round(dic["result"]["location"]["lng"]-0.011272232456079223,3)
        lat = round(dic["result"]["location"]["lat"]-0.004138259740530614,3)
        print([lng,lat])
        print(',')
    else:
        print(f"{address}:地理编码不成功")