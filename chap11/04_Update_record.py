import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('''
update phonebook set phone=?, email=? where name=?
''',('010-7777-7777','hongkd@hong.com','홍길동'))

conn.commit()

cursor.close()
conn.close()