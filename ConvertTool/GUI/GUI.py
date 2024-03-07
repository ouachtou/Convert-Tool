from tkinter import *  # Import the graphical library
import tkinter as tk
from tkinter import ttk

from Controller.Converting import converting  # Import converting function from Controller.Converting module

listEntry = []
listOutput = []
txtEntry = ""
txtOutput = ""
txtO = ''
txtE = ''

def GUI():
    global listEntry
    global listOutput
    global txtEntry
    global txtOutput
    global txtO
    global txtE

    Window = Tk()
    Window.title('ConverTool')
    Window.geometry('500x300')

    # EntryChoices
    labelChoices = tk.Label(Window, text="Entry choices: ")
    labelChoices.place(x=20, y=40)

    listeProduits = ["binary", "decimal", "hexadecimal"]
    listEntry = ttk.Combobox(Window, values=listeProduits)
    listEntry.current(0)
    listEntry.place(x=20, y=65)

    # OutputChoices
    labelChoices = tk.Label(Window, text="Output choises: ")
    labelChoices.place(x=280, y=40)

    listeProduits = ["binary", "decimal", "hexadecimal"]
    listOutput = ttk.Combobox(Window, values=listeProduits)
    listOutput.current(1)
    listOutput.place(x=280, y=65)

    # ToConvert
    txtE = StringVar()
    txtE.set("Number to convert")
    txtEntry = Entry(Window, textvariable= txtE)
    txtEntry.place(x=20, y=140)

    # ConvertButton
    Button(text='-->', command=converting).place(x=220, y=140)

    # Converted
    txtO = StringVar()
    txtO.set("Output")
    txtOutput = Entry(Window, textvariable= txtO)
    txtOutput.place(x=280, y=140)

    # Leave
    leaveButton=Button(Window, text="Fermer", command=Window.quit)
    leaveButton.place(x=400, y=250)

    Window.mainloop()
