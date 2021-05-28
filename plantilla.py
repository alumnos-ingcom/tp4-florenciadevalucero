################
# Lucero D'eva Florencia - @florenciadevalucero
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio


# def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
#     print(f"{mensaje} \nTiene 5 reintentos ")
#     
#     for i in range (cantidad_reintentos):
#         ingreso = input(f"Intento {i+1} # ")
#         try:
#             entero = int(ingreso)
#             return
#         
#         except ValueError :
#             if i ==(cantidad_reintentos-1):
#                 print("No era un número! Vuelva a intentarlo.")
#                 raise IngresoIncorrecto("No era un número!") from err
#                 return entero
            
            
        
    
def ingreso_entero_restringido(mensaje,valor_minimo=0, valor_maximo=10):
    ingreso = input(mensaje + " #")
    
    if valor
    
    

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
# def ingreso_entero(mensaje):
#     ingreso = input(mensaje + " #")
#     try:
#         entero = int(ingreso)
#     except ValueError as err:
#         raise IngresoIncorrecto("No era un número!") from err
#     return entero

if __name__ == "__main__":
#     ingreso_entero("Digite un número entero")
#     ingreso_entero_reintento("Bienvenido, digite un número entero: ", cantidad_reintentos=5)
    ingreso_entero_restringido("Ingrese un numero entro 0 y 10")