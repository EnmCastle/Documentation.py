#Es hora de divertirnos rsrs
dato = input('Ingrese un dato: ')

Lista = ['Hola', 'Mudo' 'chanchito', 'feliz']
if Lista.count(dato) > 0:
    print("El valor se encuentra dentro de nuestros registros o listas", dato)
    
else: print("El valor ingresado no estaba en nuestra lista")

#Analisis de errores con TRy

primero = int(input("Ingrese un valor: ")) #De forma predeterminada, 
#la función input() convierte la entrada en una cadena, aunque escribamos un número. 
# Si intentamos hacer operaciones, se producirá un error.
try:
     primero = int(primero / 0)
except Exception as e:
    print("EL dato recibido no es un numero: ", e)
    
except ZeroDivisionError as ex:
    print("Error de sitema tipo :", ex)
    

#https://www.mclibre.org/consultar/python/lecciones/python-entrada-teclado.html#:~:text=numero1%20%3D%20int(input(%22,%22)

#Sumadora de numeros enteros

V2 = input("Ingrese un valor: ")
try:
    V2 = int(V2)
except:
    V2 = 'Chanchito'
    
if V2 == 'Chanchito':
    print("El valor que ingresaste no es un entero, solo admitimos valores de numeros enteros")
    exit()


V1 = input("Ingrese otro valor: ")
try:
    V1 = int(V1)
except:
    V1 = 'Chanchito'

if V1 == 'Chanchito':
  print("valor  incorrecto intenta digitar solo numero y vuelve a intentarlo")
  exit()

operacion = input("Ingresa el simbolo de una operacion")
if operacion == "+":
    print(V1 + V2) 
    
elif operacion == "-":
    print( V1-V2)
    
elif operacion == "*":
    print( V1*V2)
    
elif operacion == "/":
    print( V1/V2)

#LEMBRA... Seimpre debes ver que tus string sean las
# mismas siempre que los datos esten correctos porque si no no funcionará

