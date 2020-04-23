from tkinter import *
import mysql.connector
from tkinter import messagebox
import smtplib

root = Tk(className=" Hotel Management")
root.geometry('1360x450')

Offer = StringVar()


def click_send():
    offer = Offer.get()

    if offer =='':
        messagebox.showwarning("Warning", "Incomplete Data Entry")
    else:
        alldb = mysql.connector.connect(host='localhost', user='root', password='admin', database='hotel')
        allcur = alldb.cursor()
        allcur.execute('Select Email_Id from all_data')
        res = allcur.fetchall()
        emails = []
        for i in res:
            a = list(i)
            emails.append(a[0])
        print(emails)

        for dest in emails:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.ehlo()
            s.starttls()
            subject = "I am playing with smtp(python)"
            s.login("email@gmail.com", "password")
            message = "Subject : {}\n\n{}".format(subject, offer)
            s.sendmail("email@gmail.com", dest, message)
            s.quit()


title_label = Label(root, text="---------  OFFERS EMAIL  ---------", fg='white',
                    width=80, height=2, font=('Orbitron', 17), bg="black")
title_label.grid(row=0)

blankspace = Label(root, text="\n")
blankspace.grid(row=1)

msg = Entry(root, fg='blue', textvar=Offer, font=('Arial Black', 20), width=70)
msg.grid(row=2, ipady=100)

send = Button(root, text='SEND to All', font=('Orbitron', 35), width=12, bg='green', command=click_send)
send.grid(row=3)

root.mainloop()