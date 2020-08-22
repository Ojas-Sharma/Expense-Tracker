# expense tracker
import csv
import os.path
import sqlite3 as db
from datetime import datetime
from tkinter import *

root = Tk()
root.geometry("400x600")



file_exists = os.path.isfile("csvfile.csv")
# Open database connection
conn = db.connect("expense.db")
cur = conn.cursor()
sql = '''
create table if not exists expense(field text, amount integer)'''
cur.execute(sql)
conn.commit()



def submit():
    
    conn = db.connect("expense.db")
    cur = conn.cursor()
    cur.execute("insert into expense values (:field, :amt) ",
                    {
                        'field': field.get(),
                        'amt': amt.get()
                    })
    conn.commit()
    conn.close()
    field.delete(0, END)
    amt.delete(0, END)

def query():
	# Create a database or connect to one
	conn = db.connect('expense.db')
	# Create cursor
	c = conn.cursor()

	# Query the database
	c.execute("SELECT *, oid FROM expense")
	records = c.fetchall()
	print(records)
    #Commit Changes
	conn.commit()

	# Close Connection 
	conn.close()

field = Entry(root, width = 30)
field.grid(row = 0, column = 1, padx = 20)

amt = Entry(root, width = 30)
amt.grid(row = 1, column = 1)

Fieldlabel = Label(root, text = "Enter Field")
Fieldlabel.grid(row = 0, column = 0)
f = field

Amountlabel = Label(root, text = "Enter Amount")
Amountlabel.grid(row = 1, column = 0)
a = amt


submit_btn = Button(root, text = "Add record", command = submit)
submit_btn.grid(row = 2, column = 0, columnspan = 2, pady = 10, padx = 10, ipadx = 100)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)



with open("csvfile.csv", "a+", ) as dummy:
    writer = csv.writer(dummy)
    if not file_exists:
        writer.writerow(["field", "amount"])
    writer.writerow([f, a])

#Commit Changes
conn.commit()

# Close Connection 
conn.close()

root.mainloop()