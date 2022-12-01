# Escribir un programa que nos indique cuantas vocales tiene una palabra

palabra = "HolamundoLXFAUUUU"


def Vocal(palabra):
    vocales = 0  # Las variables que solo van a ser usadas dentro de la función deben ser siempre declaradas dentro de nuestra propia función
    for x in palabra:  # metodo lower devuelve todos los caracteres en minusculas
        if x.lower() in "aeiou":
            vocales += 1
    return vocales


totalV = Vocal(palabra)
print(f"La palabra {palabra} tienen {totalV} vocales")
