#if 8 > 5: #Una pequema introducción a las condiciones
    #print("La wea Cosmica che")
    
    #Vamos a trabajar unas listas
    
lista = [3,2,3,]
lista2=lista.copy() #Nos permite copiar
lista.append(4) #Metodo append nos ayuda a agregar valores a nuestra lista.
 
#print(lista, lista2)

#Contar elementos y ver cuantas veces se repite dentro de nuestras listas

#print(lista, lista2.count(3))

#print(len(lista), len(lista2)) #La funcion len nos mostrara cuantos elementos existen dentro de nuestra lista

# Vaciar nuestra lista ---> list.clear()

#print(lista[0]) #Aqui podemos imprimir algun elemento de nuestra lista... Comenzando desde el primer elemto cuyo indice es 0
#lista.pop() ---> Aqui podemos eliminar el ultimo dato
lista.remove(2) # ---> Aqui podemos especificar algun valor que queremos eliminar
print(lista)

