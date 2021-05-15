# Lucero D'eva Florencia - @florenciadevalucero
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Escribir una función que reciba dos valores y retorne:

# Retornar -1 si el primero es menor que el segundo
# Retornar 0 si son iguales
# Retornar 1 si el primero es mayor que el segundo

import tp4_ej1 as soporte

def signo(numero):
    if numero > 0:
        print(f"El numero {numero} es positivo")
    elif numero == 0:
        print(f"El numero {numero} es cero")
    else:
        print(f"El numero {numero} es negativo")

def prueba():
    numero = soporte.ingreso_entero("Ingrese un numero: ")
    signo(numero)

if __name__ == "__main__":
    prueba()
    