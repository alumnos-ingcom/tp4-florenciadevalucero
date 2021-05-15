# Lucero D'eva Florencia - @florenciadevalucero
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

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
    