from tkinter import *

root = Tk(className=" HOTEL MANAGEMENT")
root.geometry('1920x1080')


# heading
heading_label = Label(root, text="---------  STAFF  ---------",font=('Orbitron',15),bg="black",fg="white")
heading_label.pack(fill=X)


# image
image1 = PhotoImage(file="hotel-staff-png-transparent.png")
label_image1 = Label(root, image=image1)
label_image1.pack()

root.mainloop()