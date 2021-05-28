# Lucero D'eva Florencia - @florenciadevalucero
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Escribir una función que indique con True si un numero indicado es Primo.
from tp4_ej1 import ingreso_entero
def es_primo(numero):
    contador = 1
    for i in range(2, numero):
        if (numero % i == 0):
            contador += 1
    divisores = contador
    if divisores >= 2:
        return False
    else:
        return True
    
        
def prueba():
    numero = ingreso_entero("Ingrese un numero para verificar si es primo o no: ")
    verificar = es_primo(numero)
    if verificar :
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} no es primo")

if __name__ == "__main__":
    prueba()