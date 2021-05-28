# Lucero D'eva Florencia - @florenciadevalucero
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""

    
def convertir_a_fahrrenheit(centigrados):
    try:
        centigrados = float(centigrados)
        
    except ValueError as err:
        raise IngresoIncorrecto("No era un número! No se puede hacer la conversion") from err
    
    conversion = (centigrados * 9/5) + 32
    return conversion
    
def convertir_a_centigrados(fahrenheit):
    try:
        fahrenheit= float(fahrenheit)
       
    except ValueError as err:
        raise IngresoIncorrecto("No era un número! No se puede hacer la conversion") from err
    
    conversion = (fahrenheit - 32) / (9/5)
    conversion = round(conversion, 2)
    return conversion

def prueba():
    print("Bienvenido al conversor de temperaturas!!")
    print(f"Conversion a grados Fahrenheit: ")
    centigrados = (input("\nIngrese los grados centigrados que desea convertir: "))
    resultado_fahrenheit = convertir_a_fahrrenheit(centigrados)
    print(f"La conversion de {centigrados} ° centigrados es: {resultado_fahrenheit}° fahrenheit")
        
    print(f"\nConversion a grados Centigrados: ")
    fahrenheit =(input("\nIngrese los grados fahrenheit que desea convertir: "))
    resultado_centigrados = convertir_a_centigrados(fahrenheit)
    print(f"La conversion de {fahrenheit} ° fahrenheit es: {resultado_centigrados}° centigrados")

if __name__ == "__main__":
        prueba()
    