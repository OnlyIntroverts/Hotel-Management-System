from tkinter import *

root = Tk(className=" HOTEL MANAGEMENT")
root.geometry('1920x1080')

# heading
heading_label = Label(root,text="---------  CONTACT US  ---------",font=('Orbitron',15),bg="black",fg="white")
heading_label.pack(fill=X)

image2 = PhotoImage(file="contact-us-banner-png.png")
label_image2 = Label(root, image=image2)
label_image2.pack()

image1 = PhotoImage(file="contact.PNG")
label_image1 = Label(root, image=image1)
label_image1.pack()

root.mainloop()