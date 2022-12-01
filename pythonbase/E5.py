#Escribir una funcion que nos indique si es par o impar

#Pista usa el modulo 

numero = int(input('Ingresa un numero'))

def parin(numero):
    return numero % 2 == 0

def parin(numero):
    if  numero % 2 == 0:
         return 'Este es un numero par'
    
    elif numero % 2 != 0 :
        return  'El numero:  ' +  str(numero)  +  '      es un impar'
    
    else: 
       return 'Los datos que ingresaste no son un numero entero'
        
        
        
if parin is True:
    print(f'El numero {numero} es par')  
    
else:
    print(f'O teu numero {numero} es impar')      

""" resultado = parin(numero)

print(resultado) """