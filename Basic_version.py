import csv
import os.path
import sqlite3 as db
from datetime import datetime

file_exists = os.path.isfile("csvfile.csv")
# Open database connection
conn = db.connect("expense.db")
cur = conn.cursor()
sql = '''
create table if not exists expenses(field string, amount number, date string )'''
cur.execute(sql)
conn.commit()

print("enter field")
field = input()
print("enter amount")
x = input()
amt = int(x)
date = str(datetime.now())

with open("csvfile.csv", "a+", ) as dummy:
    writer = csv.writer(dummy)
    if not file_exists:
        writer.writerow(["field", "amount"])
    writer.writerow([field, amt])

sql = ''' insert into expenses values ( '{}', {}, '{}') '''.format(field, amt, date)
cur.execute(sql)
conn.commit()