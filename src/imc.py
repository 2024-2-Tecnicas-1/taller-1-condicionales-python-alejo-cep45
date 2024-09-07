def evaluar(peso, estatura, edad):
    imc=float(peso/estatura**2)
    if((imc < 22.0) and (edad < 45)):
        return "bajo";
    elif((imc >= 22.0) and (edad < 45)):
        return "medio";
    elif((imc < 22.0) and (edad >= 45)):
        return "medio";
    else:
        return"alto";

if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
