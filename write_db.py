import pymysql

# 连接数据库
db = pymysql.connect(host="localhost",
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8'
                     )

# 创建游标
cur = db.cursor()

# 对数据库操作 （增删改查）
# 写操作（增删改）

l =[('Emma','sing',40000),
        ('Emma','sing',10000),
        ('Emma','sing',30000)]
try:


    sql = "insert into hobby (name,hobby,price) values(%s,%s,%s);"
    cur.executemany(sql,l)


    # SQL语句程序结束之前在缓存区，需要提交到数据库才能实时看到
    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# # 获取结果（一条记录）  没有结果返回None
# row = cur.fetchone()
# print(row) #(1, 'Lily', 19, 'w', 92.0)
#
# # 获取多条结果  没有结果返回（）空元组
# row = cur.fetchmany(2)
# print(row) # ((2, 'Tom', 18, 'm', 81.0), (3, 'Jason', 37, 'm', 59.0))
#
# # 获取所有结果   没有结果返回（）空元组
# row = cur.fetchall()
# print(row) # ((4, 'Brian', 22, 'm', 100.0), (5, 'Lucy', 24, 'w', 100.0), (7, 'Cherry', 20, 'o', 0.0), (8, 'Joy', 20, 'w', 95.0), (9, 'Kerry', 39, 'm', 98.0))

#cur 在查询后可以迭代取值



# 关闭游标和数据库
cur.close()
db.close()

# 练习2
# import pymysql
#
# db = pymysql.connect(host="localhost",
#                      port=3306,
#                      user='root',
#                      password='123456',
#                      database='stu',
#                      charset='utf8'
#                      )
# cur = db.cursor()

# # select_name=input("输入查询的名字：")
# # sql = "select * from cls where name='%s';"% select_name
# # cur.execute(sql)
# # row = cur.fetchone()
# # print(row)
#
#
#
# cur.close()
# db.close()
