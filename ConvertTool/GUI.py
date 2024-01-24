from tkinter import *  # import de la bibliothèque graphique
import tkinter as tk
from tkinter import ttk

Mf = Tk()
Mf.title('ConverTool')
Mf.geometry('300x200')
Mf.config(background="white")

#------------------Choix_entrée------------------#
labelChoix = tk.Label(Mf, text="Choix d'entrée:")
labelChoix.pack()

listeProduits = ["binary", "decimal", "hexadecimal"]
listeCombo = ttk.Combobox(Mf, values=listeProduits)
listeCombo.current(0)
listeCombo.pack()

#------------------Choix_sortie------------------#
labelChoix = tk.Label(Mf, text="Choix de sortie")
labelChoix.pack()

listeProduits = ["binary", "decimal", "hexadecimal"]
listeCombo = ttk.Combobox(Mf, values=listeProduits)
listeCombo.current(1)
listeCombo.pack()

#------------------ToConvert------------------#
dec=StringVar()
zone1 = Entry(Mf, textvariable= dec, bg ='purple', fg='white')
zone1.grid(row=3, column=2,pady=5)
dec.set('décimal')

#------------------Converting------------------#
Button_convert = Button(Mf, text = 'Convert',command=calcul())
Bouton_convert.grid(row=2, column=3,pady=2)


#------------------Converted------------------#
dec=StringVar()
zone1 = Entry(Mf, textvariable= dec, bg ='purple', fg='white')
zone1.grid(row=3, column=4,pady=5)
dec.set('décimal')


# bouton Quitter
Bouton1 = Button(Mf, text='Quitter la fenetre', command=Mf.destroy)
Bouton1.grid(row=6, column=0, columnspan=3, pady=5)

Mf.mainloop()
