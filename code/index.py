from flask import Flask, render_template, request,jsonify,redirect, url_for , send_file
import os
import json
import pymysql
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Gyj001202',
    db='act',
    charset='utf8'
)

@app.route('/')
def index() -> 'html':
    return render_template("index.html")

@app.route('/dataset')
def dataset() -> 'html':
    cur = conn.cursor()

    # get annual sales rank
    sql = "select * from map"
    cur.execute(sql)
    content = cur.fetchall()
    print(content)

    # 获取表头
    sql = "SHOW FIELDS FROM map"
    cur.execute(sql)
    labels = cur.fetchall()
    labels = [l[0] for l in labels]

    return render_template('dataset.html', labels=labels, content=content)

@app.route('/map')
def map() -> 'html':
    return send_file("map.html")

@app.route('/datavisual')
def datavisual() -> 'html':
    return render_template("datavisual.html")

@app.route('/find')
def find() -> 'html':
    return render_template("find.html")

@app.route('/home')
def home() -> 'html':
    return render_template("index.html")

@app.route('/findresult', methods=['POST','GET'])
def findresult():
    markers = request.data.decode('utf-8')
    print('JSON', markers)
    #
    # 转换json字符串为json（数组）对象
    markArry = json.loads(markers)
    mark = markArry[0]
    date = mark['date']
    date = date.replace("'", "\\'")
    time = mark['time']
    time = time.replace("'", "\\'")
    price = mark['price']
    area = mark['area']
    print("打印各字段值：", date, time, price, area)

    cur = conn.cursor()

    # get annual sales rank
    if price == "cheap":
        sqldata = "select name from map where price<=100 and data>=data and time<=time"
    elif price=="comfort":
        sqldata = "select name from map where price<=200 and data>=data and time<=time"
    else:
        sqldata = "select name from map where price<=1000 and data>=data and time<=time"
    cur.execute(sqldata)
    u = cur.fetchall()
    somedict = {"item": [x[0] for x in u]}
    data = json.dumps(somedict)
    print(somedict)
    return render_template('find.html',data=data)

if __name__ == '__main__':
    app.run(debug=True)