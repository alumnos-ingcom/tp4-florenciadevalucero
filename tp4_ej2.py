# Lucero D'eva Florencia - @florenciadevalucero
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Escribir una función que haga la suma entre dos números
# enteros sin hacer la operación de manera directa.
from tp4_ej1 import  ingreso_entero

def suma_lenta(numero, otro_numero):
    limite = otro_numero
    
    if otro_numero < 0:
        limite *= -1 #Esto es por si el numero ingresado es negativo y no pueda
                          # ser usado en el for como limite
    
    for i in range(limite):
        if otro_numero < 0:
            resultado = numero - i - 1
            print(f"{numero- i} + (-1) = {resultado}")
            
        else:
            resultado = numero + i + 1
            print(f"{numero+ i} + 1 = {resultado}")
            
def prueba():
    print("Suma lenta de numeros")
    numero = ingreso_entero("Ingrese un numero para sumar: ")
    otro_numero = ingreso_entero("\nIngrese otro numero: ")
    suma_lenta(numero, otro_numero)
      

if __name__ == "__main__":
    prueba()
    