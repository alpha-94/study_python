import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('select * from phonebook')

rows = cursor.fetchall() # 리턴 //메모리 접근

for row in rows:
    print('name : {0}, phone : {1}, email : {2}'.format(row[0],row[1],row[2]))

cursor.close()
conn.close()


