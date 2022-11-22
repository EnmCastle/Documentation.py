def MF():
    print("Una funcion es lo que soy")
    
    #Son bloques de codigos que se ejecutan cuando las "Llamamos"
    
MF() 

def Imp(Nombre, Apellido ): #Lo que esta definido dentro de las funciones se llama argumento
    print("Su nombre y apellidos son ", Nombre, Apellido) 

Imp(Nombre='Enmanuel', Apellido='Castillo')#Lo que esta aqui dentro de llama parametros

#Hay otras formas de definir funciones


def Funcion(*Argumentos): #El anterisco nos va a permitir digirtar
    #quantos parametros necesitemos convietiendo el 
    #Proceso en una lista
    print('Tus argumentos son :', Argumentos[3]) 
    #Ese 3 que puedes ver es el mismo atributo que usamos para extraer un valor de una lista 
    
Funcion('Addhominem','Lazos','Psicologia moderna0','Teorias conspirativas')

#La siguiente es solo otra forma de sintax para nuestra misma función de encima 

def nombrecompleto(**kwargs):
    print(kwargs['Nombre'], kwargs['Apellido'])
    
    
nombrecompleto(Nombre='Enmanuel', Apellido = 'Castillo') #Aqui lo que hicimos fue darle una chave o marca para poder especificar cada valor


#Aqui establecimos un valor predeterminado en caso de no tener parametros
def funciondef(argumentodef = 'predeterminado'): 
    print(argumentodef)
 

funciondef(argumentodef='Cometeesta')
funciondef()


#Una funcion tipo lista tambien donde podemos itinerar cada una

def listas1(lista):
    for el in lista:
        print(el)
        
listas1(['HOla','mundo','como','estan','todos'])

#Recursividad, Haremos un simple contador en reversa:

def recursiva(recurx): #DEfinimos la funcion 
    if(recurx < 1):   # Preguntamos si recurx es menor que uno 
        return recurx #retornamos en caso de que se cumpla la condicion 
    print(recurx) 
    recursiva(recurx -1) # Aqui llamamos a nuestra función solo que restandole uno al parametro que resivamos
    
recursiva(10)











   


    