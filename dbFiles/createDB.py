import sqlite3

# if this db exists the connect methods will connect, if not it will create it
conn = sqlite3.connect("pandasData.db")


try:
    # create a cursor object to assist me with executing quiries
    cur = conn.cursor()
    # create an sql query to pass to the cursor object
    cur.execute("create table player (name text, rollno integer, average real)")
    # the actual execution occurs with the commit function
    conn.commit()
except Exception as err:
    print(err)
    print("Table Already exists")

else:
    print("The table has been created")
finally:
    # close the db connection
    conn.close()
