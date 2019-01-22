import sqlite3


conn = sqlite3.connect('pandasData.db')

try:
    cur = conn.cursor()
    cur.execute("update player set rollno=8, average=66.3 where name ='Kobe Bryant' ")
    conn.commit()
    print("DB has been updated")

except Exception as err:
    print(err)
finally:
    conn.close()
