import GUI.GUI
from GUI.GUI import *
def binaire_decimal():
    toConvert = str(GUI.GUI.txtEntry.get())
    potency = 0
    total = 0
    for i in range(len(toConvert) - 1, -1, -1):
        if toConvert[i] != '0' and toConvert[i] != '1':
            return 'The value entered is not binary !'
        total += int(toConvert[i]) * (2 ** potency)
        potency += 1
    return GUI.GUI.txtO.set(str(total))


def hexa_decim():
    toConvert = str(GUI.GUI.txtEntry.get())
    conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                        'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    decimal = 0
    potency = len(toConvert) - 1
    for digit in toConvert:
        decimal += conversion_table[digit] * 16 ** potency
        potency -= 1
    return GUI.GUI.txtO.set(str(decimal))


def decimal_to_hexa():
    conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    toConvert = int(GUI.GUI.txtEntry.get())  # l'assert est déjà fait avce la transfaormation en int
    hexadecimal = ''

    while toConvert > 0:
        remainder = toConvert % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        toConvert = toConvert // 16

    return GUI.GUI.txtO.set(str(hexadecimal))


def decim_binair():
    toConvert = int(GUI.GUI.txtEntry.get())
    binary = 0
    ctr = 0
    temp = toConvert
    while (temp > 0):
        binary = ((temp % 2) * (10 ** ctr)) + binary
        temp = int(temp / 2)
        ctr += 1
    rep = binary
    return GUI.GUI.txtO.set(str(rep))


def binair_hexa():
    toConvert = str(GUI.GUI.txtEntry.get())

    for i in range(len(toConvert) - 1, -1, -1):
        if toConvert[i] != '0' and toConvert[i] != '1':
            return 'The value entered is not binary !'
    # Dictionnaire pour la correspondance des chiffres hexadécimaux
    hex_dict = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }

    # Assurer que la longueur du nombre binaire est un multiple de 4
    while len(toConvert) % 4 != 0:
        toConvert = '0' + toConvert

    # Diviser le nombre binaire en groupes de 4 chiffres
    groups_of_four = [toConvert[i:i + 4] for i in range(0, len(toConvert), 4)]

    # Convertir chaque groupe de 4 chiffres en sa représentation hexadécimale correspondante
    hex_num = ''.join(hex_dict[group] for group in groups_of_four)

    # Supprimer les zéros inutiles à gauche
    hex_num = hex_num.lstrip('0')

    # Ajouter '0' s'il n'y en a pas
    if not hex_num:
        hex_num = '0'

    # Retourner le résultat
    return GUI.GUI.txtO.set(str(hex_num))

    


def hexa_bin():
    toConvert = str(GUI.GUI.txtEntry.get())
    conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                        'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    decimal = 0
    potency = len(toConvert) - 1
    for digit in toConvert:
        decimal += conversion_table[digit] * 16 ** potency
        potency -= 1

    binary = 0
    ctr = 0
    temp = decimal
    while (temp > 0):
        binary = ((temp % 2) * (10 ** ctr)) + binary
        temp = int(temp / 2)
        ctr += 1
    rep = binary
    return GUI.GUI.txtO.set(str(rep))



