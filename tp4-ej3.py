class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    
def convertir_a_fahrrenheit(centigrados):
    try:
        centigrados = float(centigrados)
        conversion = (centigrados * 9/5) + 32
        print(f"La conversion de {centigrados}° grados centigrados son {conversion} °grados Fahrenheit") 
       
    except ValueError as err:
        raise IngresoIncorrecto("No era un número! No se puede hacer la conversion") from err    
    
def convertir_a_centigrados(fahrenheit):
    try:
        fahrenheit= float(fahrenheit)
        conversion = (fahrenheit - 32) / (9/5)
        conversion = round(conversion, 2)
        print(f"La conversion de {fahrenheit}° grados fahrenheit son {conversion} °grados Centigrados") 
       
    except ValueError as err:
        raise IngresoIncorrecto("No era un número! No se puede hacer la conversion") from err    
    


if __name__ == "__main__":
    print("Bienvenido al conversor de temperaturas!!")
    print(f"Conversion a grados Fahrenheit: ")
    convertir_a_fahrrenheit(37)
    print(f"Conversion a grados Centigrados: ")
    convertir_a_centigrados(37)
    