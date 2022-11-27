""" c = open('MODULOS.py') #Aqui nosotros podremos leer archivos
print(c.read()) #read nos permitira leer y tambien podemos dar otros permisos 
                 #como !append (O simplemente colocando una 'a' la 'w' nos va a permitir modificar el archivo)
                 #El atributo 'a' nos permite agregar datos a diferencia del atributo 'w' que nos permite
                 #modificar por completo el archivo y en caso de no existir nos lo va a crear.
                 #existe otro permiso para crear archivos en python 'x'. En caso de que ya haya un archivo da error 
#Como podemos leer solo una linea ? """

""" c.close() """

""" c = open('MODULOS.py',)

#Todos estos radline nos ayudaran a leer linea por linea de forma ordenada

print(c.readline())
c.close() """

#Nota importante tambien podemos usar for para leer cada linea por separado de nuestro archivo 

c = open('hola.txt', 'w') #En nuestra carpeta vamos a ver que se creo un hola.txt + nuestro texto de write
c.write('\nagregaremos una nueva linea al libro de drake')
c.close

#Como eliminar los archivos

# Debemos importar un modulo que esta dentro de nuestro pripio sistema opertativo llamado os """
c = open('Arquivo.txt', 'w')
import os 
if os.path.exists('Archivo.txt'): #Esta linea es para no retornar errores y esta preguntando si esxiste usando condiciones
 os.remove('Archivo.txt') #Des esta forma sera eliminado pero en caso de que no exista nos retornará un error
else:
    c.write('Arquivo.txt') #Aqui decidimos crear este arvhivo y ahora esta en nuestra carpeta
    print('El arvhico que estas tratando de eliminar no existe')

c.close()  

""" Ahora veremos eliminar carpetas enteras """
if os.path.exists('Carpetadeejemplo'): #El mismo ejemplo de comprovación de existencia de nuestra carpeta o archivo
 os.rmdir('Carpetadeejemplo')
else:
    print('Esta carpeta ya ha sido eliminada anteriormente y no existe') 
