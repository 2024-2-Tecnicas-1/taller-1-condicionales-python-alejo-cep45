def evaluar(anno):
    if((anno%100==0)and(anno%400==0)):
        return(str(anno)+" es bisiesto");
    elif((anno%4==0)and not(anno%100==0)):
        return(str(anno)+" es bisiesto");
    else:
        return(str(anno)+" no es bisiesto");

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
