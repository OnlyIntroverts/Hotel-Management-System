from tkinter import *
from subprocess import call
import mysql.connector
from tkinter import messagebox

root = Tk(className=" HOTEL MANAGEMENT")
root.geometry('1000x750')


# calling functions
def click_vacancy():
    call(["python", "vacancy.py"])


def click_developers():
    call(["python", "developers.py"])


def click_branches():
    call(["python", "branches.py"])


def click_contact_us():
    call(["python", "contact_us.py"])


def click_staff():
    call(["python", "staff.py"])


def click_allcust():
    call(['python', 'all_details.py'])


# variables
F_name = StringVar()
L_name = StringVar()
Phone = IntVar()
Email = StringVar()
Address = StringVar()
Room_no = IntVar()
Room_type = IntVar()
Room_type.set(1)
No_people = IntVar()
No_days = IntVar()


# Database Submitted
def click_submit():
    f_name = F_name.get()
    l_name = L_name.get()
    phone = Phone.get()
    email = Email.get()
    address = Address.get()
    room_no = Room_no.get()
    no_people = No_people.get()
    room_type = Room_type.get()
    no_days = No_days.get()

    if f_name == '' or l_name == '' or phone == 0 or email == '' or address == '' or room_no == 0 \
            or no_people == 0 or room_type == '' or no_days == 0:
        messagebox.showwarning("Warning", "Incomplete Data Entry")
    else:
        mydb = mysql.connector.connect(host='localhost', user='root', password='admin', database='hotel')
        alldb = mysql.connector.connect(host='localhost', user='root', password='admin', database='hotel')
        allcur = alldb.cursor()
        cur = mydb.cursor()
        cur.execute('Select Exists(select * from hotel_management where Room_No=%s)', (room_no,))
        res = cur.fetchall()
        avail = 0
        for i in res:
            a = list(i)
            avail = a[0]
        if avail == 0:
            cur.execute('INSERT INTO hotel_management'
                        '(First_Name, Last_Name, Phone_No, Email_Id, Address_No, Room_No, Room_Type, No_People, '
                        'No_Days) '
                        ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                        (f_name, l_name, phone, email, address, room_no, room_type, no_people, no_days))
            allcur.execute('INSERT INTO all_data'
                           '(First_Name, Last_Name, Phone_No, Email_Id, Address_No, Room_No, Room_Type, No_People, '
                           'No_Days) '
                           ' VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                           (f_name, l_name, phone, email, address, room_no, room_type, no_people, no_days))
            mydb.commit()
            alldb.commit()
            if no_people == 2:
                call(['python', 'second_person.py'])

            fname_entry.delete(0, 'end')
            lname_entry.delete(0, 'end')
            phone_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            ad_entry.delete(0, 'end')
            rn_entry.delete(0, 'end')

            messagebox.showinfo("Check in", "Room Allotment Successful")
            root.destroy()
        else:
            messagebox.showinfo("Room", "Room Already Occupied")
            rn_entry.delete(0, 'end')


# Menu Bar
menu_bar = Menu(root)
root.config(menu=menu_bar)
home_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Home", menu=home_menu)
home_menu.add_command(label="All Customers", command=click_allcust)
home_menu.add_separator()
home_menu.add_command(label="Vacancy", command=click_vacancy)
home_menu.add_separator()
home_menu.add_command(label="Exit", command=root.quit)

about_menu = Menu(menu_bar)
menu_bar.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="Branches", command=click_branches)
about_menu.add_separator()
about_menu.add_command(label="Staff", command=click_staff)
about_menu.add_separator()
about_menu.add_command(label="Developers", command=click_developers)

help_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Contact Us", command=click_contact_us)

# heading
heading_label = Label(root, text="---------  CUSTOMER CHECK IN FORM  ---------", font=('Orbitron', 15), bg="black",
                      fg="white")
heading_label.pack(fill=X)

black_space = Label(root, text="\n\n")
black_space.pack()

# form Design

top_frame = Frame(root)
top_frame.pack()

# Name Label
fname_label = Label(top_frame, text="First Name : ", font=('Orbitron', 20))
lname_label = Label(top_frame, text="Last Name : ", font=('Orbitron', 20))
fname_entry = Entry(top_frame, textvar=F_name, bd=5, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))
lname_entry = Entry(top_frame, bd=5, textvar=L_name, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

fname_label.grid(row=0, column=0, padx=15, pady=10, sticky=E)
lname_label.grid(row=1, column=0, padx=15, pady=10, sticky=E)
fname_entry.grid(row=0, column=1, pady=10, ipady=5, ipadx=60)
lname_entry.grid(row=1, column=1, pady=10, ipady=5, ipadx=60)

# phone number
phone_label = Label(top_frame, text="Mobile Number : ", font=('Orbitron', 20))
phone_entry = Entry(top_frame, textvar=Phone, bd=5, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

phone_label.grid(row=2, column=0, padx=15, pady=10, sticky=E)
phone_entry.grid(row=2, column=1, ipady=5, ipadx=60)

# Email Address
email_label = Label(top_frame, text="Email Address : ", font=('Orbitron', 20))
email_entry = Entry(top_frame, textvar=Email, bd=5, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

email_label.grid(row=3, column=0, padx=15, pady=10, sticky=E)
email_entry.grid(row=3, column=1, ipady=5, ipadx=60)

# Address
ad_label = Label(top_frame, text=" Address : ", font=('Orbitron', 20))
ad_entry = Entry(top_frame, bd=5, textvar=Address, bg="#ccefff", fg='blue', width=20, font=('Arial', 15))

ad_label.grid(row=4, column=0, padx=15, pady=10, sticky=E)
ad_entry.grid(row=4, column=1, ipady=5, ipadx=60)

# Room Number

rn_label = Label(top_frame, text="Room Number : ", font=('Orbitron', 20))
rn_entry = Entry(top_frame, textvar=Room_no, bd=5, bg="#ccefff", fg='blue', width=5, font=('Arial', 15))

rn_label.grid(row=5, column=0, padx=15, pady=10, sticky=E)
rn_entry.grid(row=5, column=1, ipady=5, ipadx=60, sticky=W)

# Number of Days
day_label = Label(top_frame, text="Number of Days : ", font=('Orbitron', 20))
day_box = Spinbox(top_frame, textvar=No_days, bg="#ccefff", fg='blue', from_=1, to=30, width=5, bd=5,
                  font=('Orbitron', 15))

day_label.grid(row=6, column=0, padx=15, pady=10, sticky=E)
day_box.grid(row=6, column=1, ipady=5, sticky=W)

# room Type
room_label = Label(top_frame, text="Room Type : ", font=('Orbitron', 20))
ac_rb = Radiobutton(top_frame, variable=Room_type, text="AC Room", fg='blue', font=('Arial', 12, 'bold'), value=1)
nac_rb = Radiobutton(top_frame, variable=Room_type, text="Non-AC Room", fg='blue', font=('Arial', 12, 'bold'), value=2)

room_label.grid(row=7, column=0, padx=15, pady=10, sticky=E)
ac_rb.grid(row=7, column=1, sticky=W)
nac_rb.grid(row=7, column=1, sticky=E)

# Number of Person
per_label = Label(top_frame, text="Number of People : ", font=('Orbitron', 20))
per_box = Spinbox(top_frame, textvar=No_people, bg="#ccefff", fg='blue', from_=1, to=2, width=5, bd=5,
                  font=('Orbitron', 15))

per_label.grid(row=8, column=0, padx=15, pady=10, sticky=E)
per_box.grid(row=8, column=1, ipady=5, sticky=W)

# vacancy Button
v_button = Button(top_frame, text="Vacancy", font=('ARIAL BLACK', 15), bg='#80002a',
                  fg='White', width=10, command=click_vacancy)
v_button.grid(row=5, column=1, ipadx=7, sticky=E)

# Submit Button
submit_button = Button(root, text="SUBMIT", width=15, bg="#269900", fg='Black', font=('ARIAL BLACK', 20), relief=RAISED,
                       command=click_submit)
submit_button.place(relx=0.5, rely=0.95, anchor=S)

root.mainloop()
