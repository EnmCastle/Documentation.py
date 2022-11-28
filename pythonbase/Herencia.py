# Herencia en programación se utiliza para poder reutilizar
# lo maximo posible el codigo en estructuras que sean similares.

#Hacer un programa que diga el nombre el apellido y el mensaje "HOla soy adeministrador". Ademas de eso al final diga
#Y soy el administrador de este equipamento aplicando herencia

from ClassandObject import Nombres  #Com as podemos mudar el nombre del  modulo 
                                    # IMPORTANTE CON COMAS PODEMOS ELEGIR CUALES FUNCIONES DEL MODULO (En caso de necesitar mas de uno)
Miu = Nombres("Enmanuel", "Castillo")

class Admin(Nombres):
    def supersaludo(self):
        print('Hola mi nombre es', self.nombre, "y soy admin")

admin = Admin('enmanuel','Castillo')

admin.supersaludo()
admin.imprimenom #Si usaramos la funcion de forma estatica no nos aparecereran los comandos de la clase "Padre"


#Esto es solo un ejemplo porque lo ideal es importar solo funcionalidades de la clase o eso creo
#Entonces para usar una funcionalidad de una clase padre dentro de una hija es mejor dejarla 
#Dentro de el mismo archivo .py (Las 2 clases)