# Lucero D'eva Florencia - @florenciadevalucero
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
#Escribir una función que dada una lista de valores enteros,
# retorne el menor ellos. E implementar otra función que retorne el valor
# máximo del conjunto de valores.

from tp4_ej1 import  ingreso_entero

def minimo(lista):
    min = 999999
    
    for item in lista :
        if item < min:
            min = item
    return min
    
    
def maximo(lista):
    maxi = -999999
    
    for item in lista:
        if item > maxi:
            maxi = item
    return maxi
    

def prueba():
    cantidad_elementos = ingreso_entero("¿Cuántos elementos tendrá su lista: ")
    
    if cantidad_elementos <= 0:
        print("Su lista no puede tener menor o iguales a cero elementos")
    
    mi_lista = []
    
    #Añadimos los elementos a la lista
    for i in range(cantidad_elementos):
        elemento = ingreso_entero(f"Ingrese el elemento {i+1} de la lista: ")
        mi_lista.append(elemento)
      
    numero_minimo = minimo(mi_lista)
    print(f"El numero menor de todos es: {numero_minimo}")
    
    numero_maximo = maximo(mi_lista)
    print(f"El numero mayor de todos es: {numero_maximo}")

if __name__ == "__main__":
    prueba()