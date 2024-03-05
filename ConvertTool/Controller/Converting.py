# Import all functions from Controller.Functions module
from Controller.Functions import *


# Function for conversion
def converting():
    # Import GUI module
    import GUI.GUI

    # Get entry and output choices from GUI
    entryChoice = GUI.GUI.listEntry.get()
    outputChoice = GUI.GUI.listOutput.get()

    # Determine conversion based on entry and output choices
    if entryChoice == "binary":
        if outputChoice == "decimal":
            binaire_decimal()  # Convert binary to decimal
        if outputChoice == "hexadecimal":
            binair_hexa()  # Convert binary to hexadecimal

    elif entryChoice == "decimal":
        if outputChoice == "binary":
            decim_binair()  # Convert decimal to binary
        if outputChoice == "hexadecimal":
            decimal_to_hexa()  # Convert decimal to hexadecimal

    elif entryChoice == "hexadecimal":
        if outputChoice == "binary":
            hexa_bin()  # Convert hexadecimal to binary
        if outputChoice == "decimal":
            hexa_decim()  # Convert hexadecimal to decimal

    else:
        print("Invalid choices !")  # Print error message for invalid choices
