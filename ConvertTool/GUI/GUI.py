
from tkinter import *  # import de la bibliothèque graphique
import tkinter as tk
from tkinter import ttk

Window = Tk()
Window.title('ConverTool')
Window.geometry('300x200')
Window.config(background="white")


#------------------Choix_entrée------------------#
labelChoix = tk.Label(Window, text="Choix d'entrée:")
labelChoix.pack()

listeProduits = ["binary", "decimal", "hexadecimal"]
listeCombo = ttk.Combobox(Window, values=listeProduits)
listeCombo.current(0)
listeCombo.pack()

#------------------Choix_sortie------------------#
labelChoix = tk.Label(Window, text="Choix de sortie")
labelChoix.pack()

listeProduits = ["binary", "decimal", "hexadecimal"]
listeCombo = ttk.Combobox(Window, values=listeProduits)
listeCombo.current(1)
listeCombo.pack()

#------------------ToConvert------------------#
dec=StringVar()
zone1 = Entry(Window, textvariable= dec, bg ='purple', fg='white')
zone1.grid(row=3, column=2,pady=5)
dec.set('décimal')
Window.mainloop()

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