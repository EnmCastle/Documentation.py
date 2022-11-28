
#En  un gran resumen podemos decir que las formas basicas de hacer matematicas (Aritmetica) es la misma que en C++



#if 8 > 5: #Una pequema introducción a las condiciones
    #print("La wea Cosmica che")
    
    
    #VAMOS A TRABAJAR LAS LISTAS
    
lista = ['xd','Bola','Jala',]
lista2=lista.copy() #Nos permite copiar
lista.append('Hola') #Metodo append nos ayuda a agregar valores a nuestra lista.
 
#print(lista, lista2)

#Contar elementos y ver cuantas veces se repite dentro de nuestras listas

#print(lista, lista2.count(3))

#print(len(lista), len(lista2)) #La funcion len nos mostrara cuantos elementos existen dentro de nuestra lista

# Vaciar nuestra lista ---> list.clear()

#print(lista[0]) #Aqui podemos imprimir algun elemento de nuestra lista... Comenzando desde el primer elemto cuyo indice es 0

#lista.pop() ---> Aqui podemos eliminar el ultimo dato

#lista.remove(2) # ---> Aqui podemos especificar algun valor que queremos eliminar

lista = reversed() #Esto nos permite volcar todo alreves (Reverso)  #NOTA IMPORTANTE!!!
# NO PODEMOS ORDENAR DATOS DE DIFERENTES TIPOS DEBEN SER SIEMPRE DEL MISMO TIPO CUANDO USAMOS O METODO DE sort
print(lista)
tuplas = ('itos1', 'cabeza de mojon', 'me vale vergz') #Tupla não muda seus dados como a lista

lista.sort() #Es una forma de ordenar listas ya sea en orden alfabetico o numerico pero solo puede recibir un tipo de dato
print(lista) 
print(tuplas.index('cabeza de mojon')) #Podemos pasar valores index determinados usando --> print(tuplas[0])


#Como las "tuplas" no pueden modificarse agregando elementos lo que podmos hacer es agregarlas a una lista como veremos a continuación 

listadupla = list(tuplas) #la funcion list convierte nuestras tuplas en listas que depues podremos modificar 
listadupla.append('hola soy un agregado a la lista duplas') #Aqui vemos un claro ejemplo de ello/ tomamos nuestra nueva variable que ahora es una lista y agregamos el atributo
#append

print(listadupla)

rango = range(8) #Este rango nos va a servir mas adelante cuando iniciemos con iteraciones. Solo define un rango entre uno y 8 en este caso

print(rango)