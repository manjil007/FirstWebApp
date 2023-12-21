import sqlite3

conn = sqlite3.connect('db.sqlite3')

cursor = conn.cursor()

cursor.execute('SELECT * FROM users')

results = cursor.fetchall()

cursor.close()

conn.close()