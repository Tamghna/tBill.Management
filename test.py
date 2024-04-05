
import sqlite3

conn = sqlite3.connect("bill_data.db")
cur = conn.cursor()


cur.execute("insert into bill_data_cust values ('hello' , '10212' , '120' , '21')")
conn.commit()