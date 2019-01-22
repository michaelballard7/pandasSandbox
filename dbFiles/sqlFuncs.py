import sqlite3

# if this db exists the connect methods will connect, if not it will create it
conn = sqlite3.connect("pandasData.db")
try:
    # create a cursor object to assist me with executing quiries
    cur = conn.cursor()
    # create an sql query to pass to the cursor object
    # cur.execute("select min(average) from player")
    # cur.execute("select max(average) from player ")
    # cur.execute("select avg(average) from player")
    # cur.execute("select count(average) from player")
    # cur.execute("select count(average) from player where average > 45 ")
    # cur.execute("select sum(average) from player")
    for record in cur.execute("select * from player where name in ('Michael Jordan')"):
        print(record)

    # # return values from query:
    # print(round(cur.fetchone()[0],2))
except Exception as err:
    print(err)
finally:
    # close the db connection
    conn.close()
