from tkinter import *

root = Tk(className=" HOTEL MANAGEMENT")
root.geometry('1920x1080')


# heading
heading_label = Label(root, text="---------  BRANCHES  ---------", font=('Orbitron', 15), bg="black", fg="white")
heading_label.pack(fill=X)

# image
image1 = PhotoImage(file="building_PNG11.png")
label_image1 = Label(root, image=image1)
label_image1.pack()

image2 = PhotoImage(file="building_PNG87.png")
label_image2 = Label(root, image=image2)
label_image2.pack()

image3 = PhotoImage(file="building_PNG31.png")
label_image3 = Label(root, image=image3)
label_image3.pack()

root.mainloop()
