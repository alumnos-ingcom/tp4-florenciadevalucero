# Lucero D'eva Florencia - @florenciadevalucero
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import tp4_ej1 as soporte

def suma_lenta(numero, otro_numero):
    limite = otro_numero
    limite *= (-1)
    
    for i in range(limite):
        if otro_numero > 0:
            resultado = numero + i + 1
            print(f"{numero+i} + 1 = {resultado}")
            
        else:
            resultado = numero - i - 1
            print(f"{numero-i} + (-1) = {resultado}")
            
def prueba():
    numero = soporte.ingreso_entero("Ingrese un numero para sumar: ")
    otro_numero = input("\nIngrese otro numero: ")
    suma_lenta(numero, otro_numero)
      

if __name__ == "__main__":
    prueba()
    