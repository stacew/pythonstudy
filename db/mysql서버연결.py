import pymysql as my

con = my.connect(host='localhost', port=3366,  #mysql server setting 3366 (default :3306)
            user='root', password='1234',
            db='shop'
            )

print('1, db 연결 성공.', con)

cs = con.cursor()
print('2. db 승인 후 연결 통로 만들었음.')

id = input('id >> ')
pw = input('pw >> ')
name = input('name >> ')
tel = input('tel >> ')

sql = "insert into member values('"+id+"','"+pw+"','"+name+"','"+tel+"')"

cs.execute(sql)
print('3. sql문 전송 성공.')

con.commit()
print('4. 전달한 sql문 바로 실행.')




