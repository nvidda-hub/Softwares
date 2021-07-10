from random import *
from string import ascii_lowercase, ascii_uppercase
from tkinter import *


num = "0123456789"
alphanum = ascii_lowercase + ascii_uppercase
spalphanum = alphanum + '#@!$%&*-_+=<>?/'

# method


def Create_Pass():
    TheChoice = Tchoice.get()       # get gives type of string
    if TheChoice == "":
        resultBox.delete(0.0, END)
        resultBox.insert(END, "\n-------Select the type of password you want!!------")

    length = int(pass_length.get())
    randPass = []
    for i in range(length):
        randPass.append(choice(TheChoice))
    result = "".join(randPass)
    TheResult = "\n *** Your password is  : " + result + "***"
    resultBox.delete(0.0, END)
    resultBox.insert(END, TheResult)

# GUI with tkinter
window = Tk()
window.geometry("800x500")
window.title("Random Password Generator")
window.iconbitmap(r"F:\Tutorials\software making\password generator\passowrd_gen.ico")

ProgName = Label(window, font=('Consolas', 15, 'bold'), text="Password Generator (^_^)", fg = "blue")
ProgName.grid(row=1, column=3, padx=200, pady=30)
ChooseType= Label(window, font=('Consolas', 14, 'bold'), text="Choose a type among 3 : ")
ChooseType.place(relx=0.3, rely=0.2)

Tchoice = StringVar()
NumChoice = Radiobutton(window, font=('corbel', 10, 'italic'), text='Numeric', variable=Tchoice, value=num)
NumChoice.place(relx=0.3, rely=0.3)

AlphaChoice = Radiobutton(window, font=('corbel', 10, 'italic'), text='Alpha Numeric', variable=Tchoice, value=alphanum)
AlphaChoice.place(relx=0.3, rely=0.35)

SpecialChoice = Radiobutton(window, font=('corbel', 10, 'italic'), text='Strong Password', variable=Tchoice, value=spalphanum)
SpecialChoice.place(relx=0.3, rely=0.4)

size = Label(window, text="Size", font=('Copperplate Gothic', 10, 'bold'))
size.place(relx=0.55, rely=0.35)

pass_length = Spinbox(window, from_=8, to=100)
pass_length.place(relx=0.6, rely=0.35)
pass_length.config(state="readonly")

GenButton = Button(window, text="Generate", command=Create_Pass)  # just call with
GenButton.place(relx=0.45, rely=0.6)

resultBox = Text(window, height=6, width=70)        # wrap=WORD
resultBox.place(relx=0.15, rely=0.7)

window.mainloop()       # otherwise we cannot see window
