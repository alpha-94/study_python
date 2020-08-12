import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('''
delete from phonebook where email=?
''',('hongkd@hong.com',)) # 튜플의 자료형태 (x,) 로 만들어 줘야한다 .

conn.commit()

cursor.close()
conn.close()