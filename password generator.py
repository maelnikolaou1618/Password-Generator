from tkinter import *
from tkinter.ttk import Combobox
import random
from tkinter.ttk import Radiobutton
import pyperclip
import tkinter.ttk as ttk

window = Tk()
window.title("Password Generator")
window.geometry("450x80")
window.config(bg='light blue')
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
strength = StringVar()
strength.set("Medium")

def setup():
    global drboxlength, txtpassword, txtencrypted,s
    s=ttk.Style()
    s.configure('Wild.TRadiobutton',background='light blue', foreground='dark blue', font=('Comic Sans', 11))
    lblpassword = Label(window, text="Password:", fg="dark blue", bg='light blue',font=("Comic Sans",12))
    lblpassword.grid(column=0, row=1)
    lbllength= Label(window, text="Length:",fg="dark blue", bg='light blue',font=("Comic Sans",12))
    lbllength.grid(column=0, row=0)
    lblencrypted = Label(window, text="Encrypted:", fg="dark blue", bg='light blue',font=("Comic Sans",12))
    lblencrypted.grid(column=0, row=2)
    txtencrypted = Entry(window)
    txtencrypted.grid(row=2, column=1)
    txtpassword=Entry(window)
    txtpassword.grid(column=1, row=1)
    drboxlength = Combobox(window)
    drboxlength['values']=(8,9,10,11,12)
    drboxlength.current(2)
    drboxlength.grid(column=1, row=0)
    btncopy = Button(window, text="Copy", command=copy,bg='dark blue',font=("Comic Sans",12), fg="white")
    btncopy.grid(column=3, row=1)
    btngenerate =Button(window, text="Generate", command=generate,bg='dark blue', font=("Comic Sans",12), fg="white")
    btngenerate.grid(column=2, row=1)
    btnencrypt = Button(window, text="Encrypt", command=encrypt,bg='dark blue', font=("Comic Sans",12), fg="white")
    btnencrypt.grid(column=4, row=1)
    radweak=Radiobutton(window, text="Weak", value="Weak", variable=strength, style='Wild.TRadiobutton')
    radweak.grid(column=2, row=0)
    radmedium= Radiobutton(window, text="Medium", value="Medium", variable=strength, style='Wild.TRadiobutton')
    radmedium.grid(column=3, row=0)
    radstrong = Radiobutton(window, text="Strong", value="Strong", variable=strength, style='Wild.TRadiobutton')
    radstrong.grid(column=4, row=0)

def generate():
    global txtpassword, drboxlength, strength, characters, txtencrypted, password
    txtencrypted.delete(0, 'end')
    password= ""
    r=drboxlength.get()
    length=int(r)
    s = strength.get()
    if s == "Weak":
        characters = lower
    elif s == "Medium":
        characters = upper
    else:
        characters = digits
    for i in range(0, length, 1):
        m = random.choice(characters)
        password=password + m
    txtpassword.delete(0, END)
    txtpassword.insert(0, password)

def encrypt():
    global characters, password, genpass, pos, encrypted, txtencrypted, txtpassword, tpos
    txtencrypted.delete(0, 'end')
    genpass = password
    encrypted=""
    if characters == lower:
        for i in range(0, len(genpass), 1):
            pos=characters.find(genpass[i])
            pos=pos+3
            tpos=pos%26
            encrypted=encrypted + characters[tpos]
        txtencrypted.insert(END, encrypted)
        txtencrypted.update()
    elif characters == upper:
        for i in range(0, len(genpass), 1):
            pos=characters.find(genpass[i])
            pos=pos+3
            tpos=pos%52
            encrypted=encrypted + characters[tpos]
        txtencrypted.insert(END, encrypted)
        txtencrypted.update()
    elif characters == digits:
        for i in range(0, len(genpass), 1):
            pos=characters.find(genpass[i])
            pos=pos+3
            tpos=pos%72
            encrypted=encrypted + characters[tpos]
        txtencrypted.insert(END, encrypted)
        txtencrypted.update()
def copy():
    global password
    pyperclip.copy(password)
setup()
window.mainloop()