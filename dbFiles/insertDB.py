import sqlite3

# if this db exists the connect methods will connect, if not it will create it
conn = sqlite3.connect("pandasData.db")
records = [("Kobe Bryant",24,33.3), ("Kevin Durant",35,29.2),("Lebron James",23,30.2)] #create this record using pandas

try:
    # create a cursor object to assist me with executing quiries
    cur = conn.cursor()
    # create an sql query to pass to the cursor object [singular:execute, plural:executemany]
    cur.executemany("insert into player values(?,?,?)",records)
    # the actual execution occurs with the commit function
    conn.commit()
except Exception as err:
    print(err)
    print("Table Already exists")

else:
    print("The data has been inserted")
finally:
    # close the db connection
    conn.close()
