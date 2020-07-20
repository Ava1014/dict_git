import pymysql
import re

# 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8'
                     )

# 创建游标
cur = db.cursor()

# 对数据库操作 （增删改查）
# 写操作（增删改）

# sql_create_table="create table words (id int primary key auto_increment,word varchar(30) not null,mean text);"
# cur.execute(sql_create_table)

f = open('dict.txt', 'r')
for line in f:
    result= re.findall(r"(\w+)\s+(.*)",line)
    sql_insert_word="insert into words (word,mean) values(%s,%s);"
    cur.execute(sql_insert_word,[result[0][0],result[0][1]])
    db.commit()

f.close()


cur.close()
db.close()