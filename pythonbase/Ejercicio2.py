#Ingresa nombre y apellido e ingresalo al reves

primerNombre = input("Ingrese primer nombre")
primerApellido = input("Ingrese primer apellido")
 
nombreInvertido =  '*'.join(reversed(primerNombre)) #join es un metodo que nos retorna un nuevo string y nos da posibilidades de agregar entre cada string algun elemto -, , , ; > o lo que sea
apellidoInvertido = '*'.join(reversed(primerApellido)) #La clase reversed es propia de python y nos sirve para hacer una iteracion en reversa de nuestros datos
                                                        #Algo importante es que reversed retorna un objeto "Reversed" por lo cual usamos el join para volverlo un string
print(nombreInvertido, apellidoInvertido)               #En ese caso le colocamos un * como ejemplo siempre debe llevar uno (o '' para no colocar nada)
print(type(nombreInvertido), type(apellidoInvertido))

#la función join convierte lo que le pasamos a través del input a cadena de texto, y el ''.
# lo toma como string vacío y es necesario para invocar al método.