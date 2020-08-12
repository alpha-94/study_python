import sqlite3

### test.db 파일 안에 phonebook 테이블 생성



conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('''
create table phonebook(
name char(32),
phone char(32),
email char(64) primary key);
''')

cursor.close()
conn.close()
















