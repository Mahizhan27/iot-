import sqlite3
conn=sqlite3.connect('tempdatabase.db')
cursor=conn.cursor()
cursor.execute(''' CREATE TABLE Tempdata(Temperature FLOAT,Time FLOAT,Status VARCHAR(10))''')
conn.commit()
print("Table is Created")
conn.close()