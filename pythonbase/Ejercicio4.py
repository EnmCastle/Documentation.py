#Funcion que indique si el usuario es mayor de edad
class Usuario:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

def mayor (self):
    if  self .edad > 17:
             print("EL usuario",self.nombre,'tiene',self.edad, 'y es mayor de edad' )
    else:
             print('Este usuario es menor de edad y no puede entrar')
    
usuario1 = Usuario('Enmanuel',15)
usuario2 = Usuario('Carlos',22)


resultado1 = mayor(usuario1)        
resultado2 = mayor(usuario2)  

print(type(resultado1),type(resultado2))