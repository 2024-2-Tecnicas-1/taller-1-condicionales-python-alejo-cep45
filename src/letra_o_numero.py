def evaluar(caracter):
    if((ord(caracter)>=65)&(ord(caracter)<=90)):
        return"Es letra mayúscula";
    elif((ord(caracter)>=97)&(ord(caracter)<=122)):
        return"Es letra minúscula";
    elif((ord(caracter)>=48)&(ord(caracter)<=57)):
        return"Es número";
    else:
        return"No es letra ni número";


if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
