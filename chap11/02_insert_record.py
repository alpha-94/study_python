''' ## 기본 틀
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('''

''')

cursor.close()
conn.close()
'''

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor() # 오라클 db PL_sql(고급문법) # java -> resultset 자료형

cursor.execute('''
    insert into phonebook values(?,?,?);
''', ('홍길동','010-5555-5555','hkd@hong.com'))

id = cursor.lastrowid
print(id)

cursor.execute('''
    insert into phonebook values(?,?,?);
''', ('이순신','010-6666-6666','lss@hong.com'))


id = cursor.lastrowid
print(id)

conn.commit()



cursor.close()
conn.close()