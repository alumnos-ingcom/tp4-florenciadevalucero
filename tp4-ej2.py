# Lucero D'eva Florencia - @florenciadevalucero
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def suma_lenta(numero, otro_numero):
    limite = otro_numero
    limite = (limite * -1)
    
    
    for i in range(limite):
        if otro_numero > 0:
            resultado = numero + i+1
            print(f"{numero+i} + 1 = {resultado} ")
        else:
            resultado = numero - i-1
            print(f"{numero-i} + (-1) = {resultado}")
            
        

if __name__ == "__main__":
    suma_lenta(-3,-10)