from tkinter import *
from subprocess import call
import mysql.connector
from tkinter import messagebox

root = Tk(className=" HOTEL MANAGEMENT")
root.geometry('900x600')

# variables
F_name = StringVar()
L_name = StringVar()
Phone = IntVar()
Email = StringVar()
Address = StringVar()
Room_no = IntVar()
Room_type = IntVar()
No_people = IntVar()
room_no = 0


def click_ok():
    global room_no
    room_no = Room_no.get()


# Database Submitted
def click_submit():
    f_name = F_name.get()
    l_name = L_name.get()
    phone = Phone.get()
    email = Email.get()
    address = Address.get()

    if f_name == '' or l_name == '' or phone == 0 or email == '' or address == '':
        messagebox.showwarning("Warning", "Incomplete Data Entry")

    else:
        mydb = mysql.connector.connect(host='localhost', user='root', password='admin', database='hotel')
        cur = mydb.cursor()
        alldb = mysql.connector.connect(host='localhost', user='root', password='admin', database='hotel')
        allcur = alldb.cursor()
        cur.execute('Select Room_No from hotel_management where Room_No=%s', (room_no,))
        room = cur.fetchall()
        actual_room = room[0]
        actual_room_no = list(actual_room)

        cur.execute('Select Room_Type from hotel_management where Room_No=%s', (room_no,))
        rtype = cur.fetchall()
        actual_rtype = rtype[0]
        actual_rtype_no = list(actual_rtype)

        cur.execute('Select No_Days from hotel_management where Room_No=%s', (room_no,))
        days = cur.fetchall()
        actual_days = days[0]
        actual_days_no = list(actual_days)

        cur.execute('INSERT INTO hotel_management'
                    '(First_Name, Last_Name, Phone_No, Email_Id, Address_No, Room_No, Room_Type, No_People, No_Days)'
                    ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                    (f_name, l_name, phone, email, address, int(actual_room_no[0]),
                     int(actual_rtype_no[0]), 2, int(actual_days_no[0])))
        allcur.execute('INSERT INTO all_data'
                       '(First_Name, Last_Name, Phone_No, Email_Id, Address_No, Room_No, Room_Type, No_People, No_Days)'
                       ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                       (f_name, l_name, phone, email, address, int(actual_room_no[0]),
                        int(actual_rtype_no[0]), 2, int(actual_days_no[0])))
        mydb.commit()
        alldb.commit()
        fname_entry.delete(0, 'end')
        lname_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        ad_entry.delete(0, 'end')

        messagebox.showinfo("Check in", "Room Allotment Successful")
        root.destroy()


# heading
heading_label = Label(root, text="---------  Second Person Detail ---------", font=('Orbitron', 15), bg="blue",
                      fg="white")
heading_label.pack(fill=X)

black_space = Label(root, text="\n")
black_space.pack()

# form Design

top_frame = Frame(root)
top_frame.pack()

# Room Number
rn_label = Label(top_frame, text="Room : ", font=('Orbitron', 20))
rn_entry = Entry(top_frame, textvar=Room_no, bd=5, bg="#ccefff", fg='blue', width=5, font=('Arial', 15))
rn_label.grid(row=0, column=0, padx=15, pady=10, sticky=E)
rn_entry.grid(row=0, column=1, ipady=5, ipadx=60, sticky=W)

# room button
r_button = Button(top_frame, text="ok", width=7, bg="sky blue", fg='black', font=('ARIAL BLACK', 15), relief=RAISED,
                  command=click_ok)
r_button.grid(row=0, column=1, padx=15, pady=10, sticky=E)

# Name Label
fname_label = Label(top_frame, text="First Name : ", font=('Orbitron', 20))
lname_label = Label(top_frame, text="Last Name : ", font=('Orbitron', 20))
fname_entry = Entry(top_frame, textvar=F_name, bd=5, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))
lname_entry = Entry(top_frame, bd=5, textvar=L_name, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

fname_label.grid(row=1, column=0, padx=15, pady=10, sticky=E)
lname_label.grid(row=2, column=0, padx=15, pady=10, sticky=E)
fname_entry.grid(row=1, column=1, pady=10, ipady=5, ipadx=60)
lname_entry.grid(row=2, column=1, pady=10, ipady=5, ipadx=60)

# phone number
phone_label = Label(top_frame, text="Mobile Number : ", font=('Orbitron', 20))
phone_entry = Entry(top_frame, textvar=Phone, bd=5, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

phone_label.grid(row=3, column=0, padx=15, pady=10, sticky=E)
phone_entry.grid(row=3, column=1, ipady=5, ipadx=60)

# Email Address
email_label = Label(top_frame, text="Email Address : ", font=('Orbitron', 20))
email_entry = Entry(top_frame, textvar=Email, bd=5, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

email_label.grid(row=4, column=0, padx=15, pady=10, sticky=E)
email_entry.grid(row=4, column=1, ipady=5, ipadx=60)

# Address
ad_label = Label(top_frame, text=" Address : ", font=('Orbitron', 20))
ad_entry = Entry(top_frame, bd=5, textvar=Address, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

ad_label.grid(row=5, column=0, padx=15, pady=10, sticky=E)
ad_entry.grid(row=5, column=1, ipady=5, ipadx=60)

# Submit Button
submit_button = Button(root, text="SUBMIT", width=10, bg="#269900", fg='Black', font=('ARIAL BLACK', 20), relief=RAISED,
                       command=click_submit)
submit_button.place(relx=0.5, rely=0.85, anchor=S)

root.mainloop()
