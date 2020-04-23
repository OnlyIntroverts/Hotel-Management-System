from tkinter import *
import mysql.connector

root = Tk(className=" HOTEL MANAGEMENT")
root.geometry('1920x600')

# heading
heading_label = Label(root, text="---------  ALL CUSTOMERS  ---------", font=('Orbitron', 15), bg="black", fg="white")
heading_label.pack(fill=X)

top_frame = Frame(root)
top_frame.pack()

# customer text view
text = Text(root, bd=5, bg="white", fg='blue', width=200, font=('Arial', 15))
text.place(rely=0.1)

# database
mydb = mysql.connector.connect(host='localhost', user='root', password='admin', database='hotel')
cur = mydb.cursor()
cur.execute('SELECT * from hotel_management')
result = cur.fetchall()
title = "First Name\t\t Last Name\t\t Phone Number\t\t Email id\t\t\t    Address\t\t Room No\t\t Room Type\t\t " \
        "People\t " \
        "Days\n"
text.insert(INSERT, title)
formatting = "-------------------------------------------------------------------------------------------" \
             "-------------------------------------------------------------------------------------------" \
             "------------------------------------------------------------------------------------------\n"
text.insert(INSERT, formatting)
text.insert(INSERT, formatting)
for i in result:
    a = list(i)
    rt = ''
    if a[6] == 1:
        rt = "AC"
    else:
        rt = "Non-AC"
    s = a[0] + "\t\t" + a[1] + "\t\t" + str(a[2]) + "\t\t" + a[3] + "\t\t\t   " + a[4] + "\t\t" + str(
        a[5]) + "\t\t" + rt + "\t\t " + str(a[7]) + " \t" + str(a[8]) + "\n\n"
    text.insert(INSERT, s)

root.mainloop()
