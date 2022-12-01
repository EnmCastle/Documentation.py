#Escribir un programa que nos indique cuantas vocales tiene una palabra

palabra = 'HolamundoLXFAUUUU'
vocales = 0
def Vocal(palabra):
 for x in palabra: #metodo lower devuelve todos los caracteres en minusculas
    if x.lower() in "aeiou":
       vocales += 1 
 return vocales    
    
 
totalV = Vocal(palabra)
print(f'La palabra {palabra} tienen {totalV} vocales')

