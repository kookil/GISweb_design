from flask import Flask, render_template,request
import pymysql

app = Flask(__name__)

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Gyj001202',
    db='act',
    charset='utf8'
)

@app.route('/')
def hello_world():
    cur = conn.cursor()

    # get annual sales rank
    sql = "select * from map"
    cur.execute(sql)
    content = cur.fetchall()

	# 获取表头
    sql = "SHOW FIELDS FROM map"
    cur.execute(sql)
    labels = cur.fetchall()
    labels = [l[0] for l in labels]

    return render_template('dataset.html', labels=labels, content=content)


if __name__ == '__main__':
    app.run(debug=True)

