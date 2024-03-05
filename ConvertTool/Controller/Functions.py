# Importing GUI module and its contents
import GUI.GUI
from GUI.GUI import *

# Function to convert binary to decimal
def binaire_decimal():
    # Get the input from the GUI text entry field
    toConvert = str(GUI.GUI.txtEntry.get())
    potency = 0
    total = 0
    # Loop through the binary digits from right to left
    for i in range(len(toConvert) - 1, -1, -1):
        # Check if the input contains only binary digits
        if toConvert[i] != '0' and toConvert[i] != '1':
            return 'The value entered is not binary !'
        # Calculate the decimal value
        total += int(toConvert[i]) * (2 ** potency)
        potency += 1
    # Set the result in the GUI output field
    return GUI.GUI.txtO.set(str(total))

# Function to convert hexadecimal to decimal
def hexa_decim():
    # Get the input from the GUI text entry field
    toConvert = str(GUI.GUI.txtEntry.get())
    # Dictionary for mapping hexadecimal digits to their decimal values
    conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                        'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    decimal = 0
    potency = len(toConvert) - 1
    # Convert hexadecimal to decimal
    for digit in toConvert:
        decimal += conversion_table[digit] * 16 ** potency
        potency -= 1
    # Set the result in the GUI output field
    return GUI.GUI.txtO.set(str(decimal))

# Function to convert decimal to hexadecimal
def decimal_to_hexa():
    # Conversion table for hexadecimal digits
    conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    # Get the input from the GUI text entry field
    toConvert = int(GUI.GUI.txtEntry.get())
    hexadecimal = ''
    # Convert decimal to hexadecimal
    while toConvert > 0:
        remainder = toConvert % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        toConvert = toConvert // 16
    # Set the result in the GUI output field
    return GUI.GUI.txtO.set(str(hexadecimal))

# Function to convert decimal to binary
def decim_binair():
    # Get the input from the GUI text entry field
    toConvert = int(GUI.GUI.txtEntry.get())
    binary = 0
    ctr = 0
    temp = toConvert
    # Convert decimal to binary
    while (temp > 0):
        binary = ((temp % 2) * (10 ** ctr)) + binary
        temp = int(temp / 2)
        ctr += 1
    rep = binary
    # Set the result in the GUI output field
    return GUI.GUI.txtO.set(str(rep))

# Function to convert binary to hexadecimal
def binair_hexa():
    # Get the input from the GUI text entry field
    toConvert = str(GUI.GUI.txtEntry.get())
    # Check if the input contains only binary digits
    for i in range(len(toConvert) - 1, -1, -1):
        if toConvert[i] != '0' and toConvert[i] != '1':
            return 'The value entered is not binary !'
    # Convert binary to hexadecimal
    hex_dict = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    while len(toConvert) % 4 != 0:
        toConvert = '0' + toConvert
    groups_of_four = [toConvert[i:i + 4] for i in range(0, len(toConvert), 4)]
    hex_num = ''.join(hex_dict[group] for group in groups_of_four)
    hex_num = hex_num.lstrip('0')
    if not hex_num:
        hex_num = '0'
    # Set the result in the GUI output field
    return GUI.GUI.txtO.set(str(hex_num))

# Function to convert hexadecimal to binary
def hexa_bin():
    # Get the input from the GUI text entry field
    toConvert = str(GUI.GUI.txtEntry.get())
    # Conversion table for hexadecimal digits
    conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                        'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    decimal = 0
    potency = len(toConvert) - 1
    # Convert hexadecimal to decimal
    for digit in toConvert:
        decimal += conversion_table[digit] * 16 ** potency
        potency -= 1
    binary = 0
    ctr = 0
    temp = decimal
    # Convert decimal to binary
    while (temp > 0):
        binary = ((temp % 2) * (10 ** ctr)) + binary
        temp = int(temp / 2)
        ctr += 1
    rep = binary
    # Set the result in the GUI output field
    return GUI.GUI.txtO.set(str(rep))
