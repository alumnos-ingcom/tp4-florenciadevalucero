################
# Lucero D'Eva Florencia - @florenciadevalucero
# Plantilla de ejercicio 10- palindromo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#Escribir una función que indique con True
#si una palabra o frase ingresada se trata de un palindromo. 


def es_palindromo(texto):
    texto = texto.replace(" ", "")
    palindromo = texto == texto[::-1]
    return palindromo


def prueba():
    texto = input("Ingrese una palabra para verificar si es palindromo: ")
    verificar = es_palindromo(texto)
    if verificar:
        print(f"{texto} es palindromo")
    else:
        print(f"{texto} no es palindromo")
    

if __name__ == "__main__":
    prueba()
