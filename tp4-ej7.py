# Lucero D'eva Florencia - @florenciadevalucero
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Escribir una función que mediante restas sucesivas,
# obtenga el valor del cociente y resto de dos números enteros.

import tp4_ej1 as soporte
def division_lenta(dividendo, divisor):
    cociente = 0
    
    if divisor == 0:
        print("No esta definida la división por 0")
    
    while dividendo >= divisor:
        dividendo =dividendo - divisor
        cociente = cociente + 1
    resto = dividendo
    
    print(f" El resto de la division  es: {resto}")
    print(f"El cociente de la division es: {cociente}")

def prueba():
    dividendo = soporte.ingreso_entero("Ingrese el numero que desea dividir: ")
    divisor = soporte.ingreso_entero("Ingrese el numero por el cual va a dividir: ")
    
    resultado = division_lenta(dividendo, divisor)
    

if __name__ == "__main__":
    prueba()