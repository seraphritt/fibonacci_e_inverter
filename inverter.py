entrada = input("Informe a string: ")


def inverter(string):
    invertida = ""
    for i in range(-1, (len(string) + 1)*-1, -1):
        invertida += string[i]
    return invertida


print(inverter(entrada))
