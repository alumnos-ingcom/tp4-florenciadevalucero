# Lucero D'eva Florencia - @florenciadevalucero
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Escribir una función que reciba dos valores y retorne:
# Retornar -1 si el primero es menor que el segundo
# Retornar 0 si son iguales
# Retornar 1 si el primero es mayor que el segundo

import tp4_ej1 as soporte

def compara(numero, otro_numero):
    if numero < otro_numero:
        return -1
    elif numero == otro_numero:
        return 0
    else:
        return 1

def prueba():
    print("Ingrese dos numeros para comparar")
    numero = soporte.ingreso_entero("Ingrese un numero: ")
    otro_numero = soporte.ingreso_entero("Ingrese otro numero: ")
    resultado = compara(numero, otro_numero)
    print(f"Resultado:  {resultado}")
         
        
        

if __name__ == "__main__":
    prueba()
    


