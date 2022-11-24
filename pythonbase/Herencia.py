# Herencia en programación se utiliza para poder reutilizar
# lo maximo posible el codigo en estructuras que sean similares.

#Hacer un programa que diga el nombre el apellido y el mensaje "HOla soy adeministrador". Ademas de eso al final diga
#Y soy el administrador de este equipamento aplicando herencia



class Admin(Nombres):
    def supersaludo(self):
        print('Hola mi nombre es', self.nombre, "y soy admin")

admin = Admin('enmanuel','Castillo')
admin.imprimenom()
admin.supersaludo()