# Lucero D'eva Florencia - @florenciadevalucero
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Escribir una función que reciba un número e indique
#si el mismo es positivo, negativo o cero.
from tp4_ej1 import  ingreso_entero

def compara(numero, otro_numero):
    if numero < otro_numero:
        return -1
    elif numero == otro_numero:
        return 0
    else:
        return 1

def prueba():
    print("Ingrese dos numeros para comparar")
    numero = ingreso_entero("Ingrese un numero: ")
    otro_numero = ingreso_entero("Ingrese otro numero: ")
    resultado = compara(numero, otro_numero)
    print(f"Resultado:  {resultado}")
         
        
        

if __name__ == "__main__":
    prueba()
    


