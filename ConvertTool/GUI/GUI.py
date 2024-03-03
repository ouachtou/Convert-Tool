# coding: utf-8
import string
from tkinter import *

fenetre = Tk()

label = Label(fenetre, text="Hello World")
label.pack()

# entrée
value = StringVar()
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=string, width=30)
entree.pack()

liste = Listbox(fenetre)
liste.insert(1, "Python")
liste.insert(2, "PHP")
liste.insert(3, "jQuery")
liste.insert(4, "CSS")
liste.insert(5, "Javascript")

liste.pack()

# bouton de sortie
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

fenetre.mainloop()