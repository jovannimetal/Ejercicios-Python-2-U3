def mysplit(strng):
    salida = []
    cadena = str()
    for letra in strng:
        if letra != ' ':
            cadena += letra
        else:
            if cadena == '':
                continue
            else:
                salida.append(cadena)
                cadena = ''
                continue
    return salida
    
print(mysplit("Ser o no ser, esa es la pregunta"))
print(mysplit("Ser o no ser,esa es la pregunta"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))