import sqlite3

# if this db exists the connect methods will connect, if not it will create it
conn = sqlite3.connect("pandasData.db")


try:
    # create a cursor object to assist me with executing quiries
    cur = conn.cursor()
    # create an sql query to select an item to the cursor object
    cur.execute("select name from player")
    # print(cur.fetchone())

    # print("Printed many items ", cur.fetchmany(4))

    # for record in cur.fetchall():
    #     print(record[0])

    # data = list(cur.execute("select * from player"))
    # for i in range(0,len(data)):
    #     for record in data:
    #         print(record[i])

    # for record in cur.execute("select * from player where name is 'Lebron James'"):
    #     print("The best player in the world", record[0])

    # for record in cur.execute("select * from player where average > 26.0"):
    #     print("A top scorer league history:", record[0], "He averaged:",record[2],"pts a season")

    for record in cur.execute("select * from player order by average desc"):
        print("Top Scorers ranked all time:",record[0],"Pts Avg:",record[2])

except Exception as err:
    print(err)
finally:
    # close the db connection
    conn.close()
