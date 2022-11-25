""" """ #La orientación a objetos se basa en objetos clases y tambien herencias
#Creamos una clase

# class Usuario: !!!!
#     nombre = 'Felipe' #Aqui indicamos los metodos o propiedades
#     apellido = 'Castillo'
    
# usuario = Usuario() 

# print(usuario.nombre, usuario.apellido) !!!!!


# Ahora vamos a crear una clase de verdad para conectarla a una base de datos imaginaria. """

class Usuario:
    def __init__(self, nombre,apellido): #El método __init__ es un método especial
                                        #de una clase en Python. El objetivo fundamental del método __init__
                                        # es inicializar los atributos del objeto que creamos.


        self.nombre = nombre
        self.apellido = apellido
usuario = Usuario('Enmanuel', 'Castillo')
usuario2 = Usuario('Luana', 'mendosa')

print(usuario.nombre,usuario.apellido,usuario2.nombre,usuario2.apellido) 
  
  #Practicas

class PersonajesL:
    def __init__(skill,HP,CH,RE): #El metodo __Init__ lo que nos va a permitir es ingresar los parametros de las instancias sin 
                                #Nececidad de tener un codigo demasiado grande
        skill.HP = HP
        skill.CH = CH
        skill.RE = RE
         
    def presentacion(skill): #Aqui estamos usando el self 'skill' para conseguir tomar argumentos de nuestra propiedad inicial 
        print('El personaje que has elegido posee las siguientes habilidades: ','HP',skill.HP,'CH',skill.CH,'RE',skill.RE)
         
         
Saldi = PersonajesL(25,10,1)
NinjaPrinc = PersonajesL(150,200,5)

Saldi.presentacion() #Muy importante no olvidar que a la hora de hacer una llamada a un metodo con nuestro objeto (O instancia) 
                     #Debemos colocar nuestro objeto 

NinjaPrinc.presentacion()




class Nombres:
    def __init__(self, nombre, apellido): #IMPORTANTE ESE PRIMER ARGUMENTO LO QUE HACE ES REFERENCIA A LA INSTANCIA
                                          #Lo mas correcto supuestamente usar self xd en todas los argumentos (REF)
        self.nombre = nombre
        self.apellido = apellido
    
    def imprimenom(self):
        print('Su nombre y su apellidos son: ',self.nombre,self.apellido)
        
usuarios = Nombres('Enmanuel', 'Castillo')
usuario2 = Nombres('Valerio','Lorazno')
    
usuarios.imprimenom()
usuarios.nombre = 'Carlitos' #De esta forma podemos cambiar los parametros cuando queramos 
usuarios.imprimenom()
""" del usuarios.nombre #DE esta forma podemos eliminar un parametro de nuestra instancia
del usuario #Y esta es la forma de eliminar un objeto  """
usuarios.imprimenom()


        
    
        
    