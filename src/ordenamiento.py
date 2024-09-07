def evaluar(numero1, numero2, numero3, numero4):
    numeros=[]
    numeros.append(numero1)
    numeros.append(numero2)
    numeros.append(numero3)
    numeros.append(numero4)
    for i in range(len(numeros)-1):
        for j in range(len(numeros)-1-i):
            if(numeros[j]>numeros[j+1]):
                mn=numeros[j];
                numeros[j]=numeros[j+1];
                numeros[j+1]=mn;
                
    return str(numeros).replace(",",'').replace("[",'').replace("]",'');

if __name__ == '__main__':
    print("Número 1:", end="")
    numero1 = int(input())
    print("Número 2:", end="")
    numero2 = int(input())
    print("Número 3:", end="")
    numero3 = int(input())
    print("Número 4:", end="")
    numero4 = int(input())
        
    respuesta = evaluar(numero1, numero2, numero3, numero4)
    print(respuesta)
