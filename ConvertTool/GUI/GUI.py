
from tkinter import *  # import de la bibliothèque graphique
import tkinter as tk
from tkinter import ttk

from Controller.Converting import converting


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


    #------------------EntryChoices------------------#
    labelChoices = tk.Label(Window, text="Entry choices: ")
    labelChoices.pack()

    listeProduits = ["binary", "decimal", "hexadecimal"]
    listEntry = ttk.Combobox(Window, values=listeProduits)
    listEntry.current(0)
    listEntry.pack()

    #------------------OutputChoices------------------#
    labelChoices = tk.Label(Window, text="Output choises: ")
    labelChoices.pack()

    listeProduits = ["binary", "decimal", "hexadecimal"]
    listOutput = ttk.Combobox(Window, values=listeProduits)
    listOutput.current(1)
    listOutput.pack()


    #------------------ToConvert------------------#
    txtE = StringVar()
    txtE.set("Number to convert")
    txtEntry = Entry(Window, textvariable= txtE)
    txtEntry.pack()

    #------------------ConvertButton------------------#
    Button(text='-->', command=converting).pack()


    #------------------Converted------------------#
    txtO = StringVar()
    txtO.set("Output")
    txtOutput = Entry(Window, textvariable= txtO)
    txtOutput.pack()

    #------------------Leave------------------#
    leaveButton=Button(Window, text="Fermer", command=Window.quit)
    leaveButton.pack()


    Window.mainloop()