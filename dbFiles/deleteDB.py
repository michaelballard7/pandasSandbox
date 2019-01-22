import sqlite3

conn = sqlite3.connect('pandasData.db')

try:
    cur = conn.cursor()
    cur.execute("delete from player where name ='Kobe Bryant' ")
    conn.commit()
    print("DB item has been deleted")

except Exception as err:
    print(err)
finally:
    conn.close()
