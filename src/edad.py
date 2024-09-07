from time import localtime

def evaluar(dia, mes, anno):
    t = localtime()
    dian = t.tm_mday
    mesn = t.tm_mon
    annon = t.tm_year
    e= annon-anno
    if(((mes>=mesn)and(dia>=dian))):
        e=e-1
    return ("Usted tiene "+str(e)+" años");

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
