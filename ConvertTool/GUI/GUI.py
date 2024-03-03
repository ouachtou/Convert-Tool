
from tkinter import *  # import de la bibliothèque graphique
import tkinter as tk
from tkinter import ttk

Window = Tk()
Window.title('ConverTool')
Window.geometry('500x300')


#------------------Choix_entré------------------#
labelChoices = tk.Label(Window, text="Choix d'entrée:")
labelChoices.pack()

listeProduits = ["binary", "decimal", "hexadecimal"]
listEntry = ttk.Combobox(Window, values=listeProduits)
listEntry.current(0)
listEntry.pack()

#------------------Choix_sortie------------------#
labelChoices = tk.Label(Window, text="Choix de sortie")
labelChoices.pack()

listeProduits = ["binary", "decimal", "hexadecimal"]
listOutput = ttk.Combobox(Window, values=listeProduits)
listOutput.current(1)
listOutput.pack()

#------------------ToConvert------------------#
txt = StringVar()
txt.set("Number to convert")
txtEntry = Entry(Window, textvariable= txt)
txtEntry.pack()

#------------------ConvertButton------------------#
Button(text='-->').pack()

#------------------Converted------------------#
txt = StringVar()
txt.set("Output")
txtOutput = Entry(Window, textvariable= txt)
txtOutput.pack()
Window.mainloop()


#------------------ToConvert------------------#
"""dec=StringVar()
zone1 = Entry(Window, textvariable= dec, bg ='purple', fg='white')
zone1.grid(row=3, column=2,pady=5)
dec.set('décimal')"""

#------------------Converting------------------#
"""Button_convert = Button(Window, text = 'Convert',command=calcul())
Bouton_convert.grid(row=2, column=3,pady=2)"""


#------------------Converted------------------#
dec=StringVar()
zone1 = Entry(Window, textvariable= dec, bg ='purple', fg='white')
zone1.grid(row=3, column=4,pady=5)
dec.set('décimal')


# bouton Quitter
Bouton1 = Button(Window, text='Quitter la fenetre', command=Window.destroy)
Bouton1.grid(row=6, column=0, columnspan=3, pady=5)

Window.mainloop()