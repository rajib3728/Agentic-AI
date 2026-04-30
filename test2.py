import sqlite3 as sq
conn=sq.connect("store.db")
cur=conn.cursor()
sql1="CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY, name TEXT, price REAL)"
cur.execute(sql1)
sql2="INSERT INTO products(name, price) VALUES('fgjk', 999.99)"
cur.execute(sql2)
sql3="INSERT INTO products(name, price) VALUES('fggf', 499.99)"
cur.execute(sql3)
conn.commit()


cur.execute("SELECT * FROM products")
l=cur.fetchall()
l.sort()
print(l)
conn.close()
