from GUI.GUI import txtEntry
from GUI.GUI import txtOutput

def binaire_decimal():
    toConvert = str(txtEntry.get())
    potency = 0
    total = 0
    for i in range(len(toConvert) - 1, -1, -1):
        if i != 0 and i != 1:
            assert False, "The value entered is not binary !"
        total += int(toConvert[i]) * (2 ** potency)
        potency += 1
    return txtOutput.set(str(total))


def hexa_decim():
    toConvert = str(txtEntry.get())
    conversion_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                        'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    decimal = 0
    potency = len(toConvert) - 1
    for digit in toConvert:
        decimal += conversion_table[digit] * 16 ** potency
        potency -= 1
    return txtOutput.set(str(decimal))


def decimal_to_hexa():
    conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    toConvert = int(txtEntry.get())  # l'assert est déjà fait avce la transfaormation en int
    hexadecimal = ''

    while toConvert > 0:
        remainder = toConvert % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        toConvert = toConvert // 16

    return txtOutput.set(str(hexadecimal))


def decim_binair():
    toConvert = int(txtEntry.get())
    binary = 0
    ctr = 0
    temp = toConvert
    while (temp > 0):
        binary = ((temp % 2) * (10 ** ctr)) + binary
        temp = int(temp / 2)
        ctr += 1
    rep = binary
    return txtOutput.set(str(rep))


def binair_hexa():
    toConvert = int(txtEntry.get())
    if toConvert != 0 and toConvert != 1:
        assert False, "The value entered is not binary !"
    hex = 0
    mul = 1
    chk = 1
    i = 0
    hnum = []
    while toConvert != 0:
        rem = toConvert % 10
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
        toConvert = int(toConvert / 10)
    if chk != 1:
        hnum.insert(i, chr(hex + 48))
    if chk == 1:
        i = i - 1

    while i >= 0:
        print(end=hnum[i])
        i = i - 1

    return txtOutput.set(str(hnum))


def hexa_bin():
    toConvert = str(txtEntry.get())
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
    return txtOutput.set(str(rep))



