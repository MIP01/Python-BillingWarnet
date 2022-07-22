from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk,Image
import os

root = Tk()
root.title('π warnet')

root.state('normal')
root.resizable(False, False)

my_img1 = ImageTk.PhotoImage(Image.open("Image/1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("Image/2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("Image/3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("Image/4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("Image/5.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=5)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=5)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=4)
    
def back(image_number):
    global my_label
    global button_forward
    global button_back


    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))


    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)
        

    my_label.grid(row=0, column=0, columnspan=5)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=4)


def file_opener():
    #set to correct destination
    history = 'history.txt'
    os.system('"%s"' % history)

def about_opener():
    #set to correct destination
    about = 'about.txt'
    os.system('"%s"' % about)

def open_billing():
    #set to correct destination
    billing = 'billing.py'
    os.system('"%s"' % billing)
    
button_history = Button(root, text="π History", command= lambda:file_opener())
button_billing = Button(root, text="Billing Warnet", command= lambda:open_billing())
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_forward = Button(root, text=">>", command=lambda: forward(2))
lbl_cp = Button(root, text="copyright @ π Team", command= lambda:about_opener())

button_history.grid(row=1, column=1)
button_billing.grid(row=1, column=3)
button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=4)
lbl_cp.grid(row=1, column=2)



root.mainloop()
