from tkinter import *
from dateline import date

root = Tk()
root.title('Getting started withg widgets')
root.geomentry('400x300')

lbl = Label(text="hey There!,fg=""white", bg="#072F5F", height=1, width=300)

name_lbl = Label(text="full name", bg="#389503")
name_entry = Entry()

def display():
    name = "welcome to the application \ntoday's date is: "
    global Message
    message = ""