from tkinter import *

root = Tk(className=" HOTEL MANAGEMENT")
root.geometry('1920x1080')


# heading
heading_label = Label(root,text="---------  DEVELOPERS  ---------",font=('Orbitron',15),bg="black",fg="white")
heading_label.pack(fill=X)


# image
image1= PhotoImage(file = "rahul.png")
label_for_image1 = Label(root, image=image1)
label_for_image1.pack(side=RIGHT)

# image
image2= PhotoImage(file = "mishika.png")
label_for_image2 = Label(root, image=image2)
label_for_image2.pack(side=LEFT)

# NAME LABELS
m_label=Label(root,text="Mishika Shukla",font=('Orbitron',20))
r_label=Label(root,text="Rahul Kumar Mishra",font=('Orbitron',20))

m_label.place(relx=0.057,rely=0.165)
r_label.place(relx=0.77,rely=0.165)

root.mainloop()