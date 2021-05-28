################
# Florencia Lucero D'eva- @florenciadevalucero
# Plantilla de ejercicio 10
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Escribir una función que retorne
#una tuple con factores primos de un numero entero positivo.
from tp4_ej1 import ingreso_entero
def factores_primos(numero):
    lista = []
    divisor = 2 #Hacemos que arranque dividiendo por 2
                    #ya que todos se pueden dividir por 1
    while numero >= divisor:
        if numero % divisor == 0:
            numero = numero / divisor
            lista.append(divisor)
        else:
            contador = contador + 1 #si el resto de dividir por dos no es 0, dividira por 3
                                                # y asi sucesivamente
    tupla_factores = (lista)
    return tupla_factores
    

def prueba():
    numero = ingreso_entero("Ingrese un numero para descomponer en factores primos: ")
    
    if numero > 0:
        tupla =factores_primos(numero)
        
        

if __name__ == "__main__":
    prueba()
