#Vamos con las condicionales. La verdad no son diferentes de otros tipos de condiones en las que hemos trabajado antes 
if 2 < 5:
    print("2 es menor que 5")
    
# Evaluaciones de variables:

b = 0
a = 0
Igualdad = a == b

a < b 

a > b 

a >= b

a >= b 

a != b # Esta retorna falso o verdadero distinto de 

# Todo usando if 


#Funciones if, elif, else... (Orden de ejecución )
#if ya lo conocemos com qualquier condicional anterior podemos usarlo ahora
#elif podemos usarlo como consecuencia en caso de que if sea = a false
# Una cosa curiosa de el es que puede anidarse cuantas veces sea necesario para luego 
# terminar con la posibilida de agregar um else al final pero siempre elif se ejecutrara antes que else
#De esa forma funciona el orden y es el mismo que tenemos arriba

#Exemplo 

if 5 < 4:
    print('Esto no se va imprimir')
elif  5 < 4: 
    print('4 es menor que 5')
    
elif 5 > 4:
    print("Ahora me ejeutaré yo porque el if y el primer elif fueron falsos")
    
else:
    print('Yo me ejecuto siempre y cuando las condiciones de if y elif sean falsas como en este caso ', 
        "Si alguna es verdadera entonces yo no me ejecutaré ")  
    
     
#Juega con los valores de arriba para aprender a usarlos



# Podemos fazer uma condicional em uma linha só 
print("Se ejecuto la condicion if 5 mayor que 2") if 5 < 2  else print("Se ejecuto la alternativa else")

#Condiciones and e or (Ja sabemos como funcionan pero voy a dejar un ejemplo)

if a == 2 and a == a:
    print("Si ves esto ambos valores eran iguales")
else: 
    print("Los valores  se mostraran porque ambos no fueron falsos ")
    
if 1 == 0 or 1 > 0:
    print("Una de las 2 condiones devolvio true")