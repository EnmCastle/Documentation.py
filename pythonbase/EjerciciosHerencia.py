#Faz um programa que registre 3 animais com seu onomatopeya e com a sua especie animalvIOLÃO STRINGBE

class Animal:
    def __init__(self,nombre,onomatopeya): #Primero incializamos nuestras instancias en init
        self.nombre = nombre
        self.onomatopeya = onomatopeya #Definimos nuestros parametros con su respectivo identificardor self (Ya se que no es un identificador)
        
    def saludo(self): #Definimos el funcionamiento de nuestra función 
         print('Hola soy un',self.tipo,'y el sonido que hago es:', self.onomatopeya,'Un dato curioso de mi es que tengo ', self.patas,'patas')
        
class Gato(Animal): #Vamos creando nuestras diferentes clases y Auqi acabamos de agregar un tipo
    tipo = "Gato" #  simplemente con el un = ya que nuestra clase ya hizo referencia a Animal
    patas = '4'
class Perro(Animal):
    tipo = "Perro"
    patas = '4'
class Canario(Animal):
    tipo = "Canario"
    patas = '2'
    
    
animalgato = Gato('Pantera','Guao digo miau') #Llego la hora de instanciar nuestros objetos

animalperro = Perro('Perro intenso','waoo :0')

animalcanario = Canario('Canario', 'Ella pasa por el bloque un piripiropi opi bopi un piripirope')


animalgato.saludo()

animalperro.saludo()

animalcanario.saludo()
