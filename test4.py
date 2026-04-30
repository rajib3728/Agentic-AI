import sqlite3 as sq
conn=sq.connect("store.db")
cur=conn.cursor()
cur.execute("DELETE FROM products")
conn.commit()
conn.close()