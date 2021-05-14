################
# Lucero D'eva Florencia - @florenciadevalucero
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""


def ingreso_entero(mensaje):
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    return entero

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    print(f"{mensaje} \nTiene 5 reintentos ")
    
    for i in range (cantidad_reintentos):
        ingreso = input(f"Intento {i+1} # ")
        try:
            entero = int(ingreso)
            print(f"Ingreso numero correcto en: {i+1} intentos")
            return
        
        except ValueError :
            if i ==(cantidad_reintentos-1):
                print(f"Tuvo {cantidad_reintentos} intentos, ya no tiene mas reintentos")
                raise IngresoIncorrecto("No era un número!") from err
        

def ingreso_entero_restringido(mensaje,valor_minimo=0, valor_maximo=10):
    print(f"{mensaje} {valor_minimo} y {valor_maximo}: ")
    ingreso =input(" #")
    try:
        entero = int(ingreso)
        if entero < valor_minimo or entero > valor_maximo:
            print(f"El numero {ingreso} no es un numero que este entre 0 y 10")
        else:
            print(f"El numero esta entre 0 y 10")
            return entero
    except ValueError:
        print("No era un número! Vuelva a intentarlo.")
    return entero



if __name__ == "__main__":
    print("Primera función\n")
    ingreso_entero("Digite un número entero")
    print("Segunda funcion\n")
    ingreso_entero_reintento("Bienvenido, digite un número entero: ", cantidad_reintentos=5)
    print("Tercera funcion\n")
    ingreso_entero_restringido("Ingrese un numero que este entre: ")
    