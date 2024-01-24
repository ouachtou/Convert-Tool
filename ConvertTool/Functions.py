from math import *

import GUI
from GUI import *
def binaire_decimal():
    h = str(bina.get())
    puissance = 0
    total = 0
    for i in range(len(h) - 1, -1, -1):
        if i != 0 and i != 1:
            assert False, ("La valeur entrée n'est pas du binaire !")
        total += int(h[i]) * (2 ** puissance)
        puissance += 1
    return dec.set(str(total))


def hexa_decim():
    hexadecimal = str(hexa.get())
    conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                        'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    decimal = 0
    puissance = len(hexadecimal) - 1
    for digit in hexadecimal:
        decimal += conversion_table[digit] * 16 ** puissance
        puissance -= 1
    return dec.set(str(decimal))


def decimal_to_hexa():
    conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    decimal = int(dec.get())  # l'assert est déjà fait avce la transfaormation en int
    hexadecimal = ''

    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16

    return hexa.set(str(hexadecimal))


def decim_binair():
    decimal = int(dec.get())
    binary = 0
    ctr = 0
    temp = decimal
    while (temp > 0):
        binary = ((temp % 2) * (10 ** ctr)) + binary
        temp = int(temp / 2)
        ctr += 1
    rep = binary
    return bina.set(str(rep))


def binair_hexa():
    bnum = int(bina.get())
    if bnum != 0 and bnum != 1:
        assert False, ("Attention, ce n'est pas du binaire !")
    hex = 0
    mul = 1
    chk = 1
    i = 0
    hnum = []
    while bnum != 0:
        rem = bnum % 10
        hex = hex + (rem * mul)
        if chk % 4 == 0:
            if hex < 10:
                hnum.insert(i, chr(hex + 48))
            else:
                hnum.insert(i, chr(hex + 55))
            mul = 1
            hex = 0
            chk = 1
            i = i + 1
        else:
            mul = mul * 2
            chk = chk + 1
        bnum = int(bnum / 10)
    if chk != 1:
        hnum.insert(i, chr(hex + 48))
    if chk == 1:
        i = i - 1

    while i >= 0:
        print(end=hnum[i])
        i = i - 1

    return hexa.set(hnum)


def hexa_bin():
    hexadecimal = str(hexa.get())
    conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                        'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    decimal = 0
    puissance = len(hexadecimal) - 1
    for digit in hexadecimal:
        decimal += conversion_table[digit] * 16 ** puissance
        puissance -= 1

    binary = 0
    ctr = 0
    temp = decimal
    while (temp > 0):
        binary = ((temp % 2) * (10 ** ctr)) + binary
        temp = int(temp / 2)
        ctr += 1
    rep = binary
    return bina.set(str(rep))



