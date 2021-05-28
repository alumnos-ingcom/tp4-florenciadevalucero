# Lucero D'eva Florencia - @florenciadevalucero
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Escribir una función que a partir de tres variables de tipo entero
# retorne una tupla con dichos valores ordenados de menor a mayor.
# Y Viceversa Interfaz
from tp4_ej6 import maximo, minimo
from tp4_ej1 import  ingreso_entero



def ordenar_mayor_a_menor(uno, dos, tres):
    mi_lista = [uno, dos, tres]
    mayor = maximo(mi_lista)
    menor = minimo(mi_lista)
    suma = uno + dos + tres
    numero_del_medio = suma - (mayor + menor)
    
    tupla = (mayor, numero_del_medio, menor)
    return tupla
    
    
    
def ordenar_menor_a_mayor(uno, dos, tres):
    mi_lista = [uno, dos, tres]
    mayor = maximo(mi_lista)
    menor = minimo(mi_lista)
    suma = uno + dos + tres
    numero_del_medio = suma - (mayor + menor)
    
    tupla = (menor, numero_del_medio, mayor)
    return tupla



def prueba():
    
    uno = ingreso_entero("Ingrese un numero para ordenar: ")
    dos = ingreso_entero("Ingrese otro numero para ordenar: ")
    tres = ingreso_entero("Ingrese otro numero para ordenar: ")
    tupla_decreciente = ordenar_mayor_a_menor(uno, dos, tres)
    print("Orden decreciente: ")
    print(tupla_decreciente)
    tupla_creciente = ordenar_menor_a_mayor(uno, dos, tres)
    print("Orden creciente: ")
    print(tupla_creciente)
    
    
    
   
    

if __name__ == "__main__":
        prueba()