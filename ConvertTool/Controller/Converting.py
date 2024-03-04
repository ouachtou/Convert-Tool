from Controller.Functions import *
from GUI.GUI import listEntry
from GUI.GUI import listOutput




def converting():
    entryChoice = listEntry.get()
    outputChoice = listOutput.get()

    if entryChoice == "binary":
        if outputChoice == "decimal":
            binaire_decimal()
        if outputChoice == "hexadecimal":
            binair_hexa()

    elif entryChoice == "decimal":
        if outputChoice == "binary":
            decim_binair()
        if outputChoice == "hexadecimal":
            decimal_to_hexa()

    elif entryChoice == "hexadecimal":
        if outputChoice == "binary":
            hexa_bin()
        if outputChoice == "decimal":
            hexa_decim()
    else:
         print("Invalid choices !")
