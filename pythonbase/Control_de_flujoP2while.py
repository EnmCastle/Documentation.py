# Ya sabemos que son los loops vamos a estudiar por medio de ejemplos 

#Haz un contador que vaya del 0 al 10 

dato0 = 0

""" while dato0 <= 10:
      print(dato0)
      if dato0 == 5:
       break #ESte atributo brake es para detener nuestro loop
      else: dato0 += 1  
       """
      #COmo detener loops usando !break! + continue

while dato0 <= 9:
    dato0 += 1
    if dato0 == 5:
        continue
    print(dato0)

   #Recuerda identar bien a la hora de probar

# for loop -------------------------->

Usuarios = ["CHanchito feliz", "Felipe", "roberto", "Nicolas"]

for Usuarios in Usuarios:
    print(Usuarios)

#Podemos incluso iterar strings
#Otra cosa que podemos hacer es hacer quiebras de codigo usando brake como en el ejemplo que sigue

Karaota = "Holamundo"

for c in Karaota:
      if c == "m":
            break
      print(c)      
      
#Usando coninue dentro dos loops a gente pode vai saltar o codigo que esteja direitamente frente ao nosso atributo
continuar = ['Gastos', 'perros', 'monos']

for x in continuar:
      if x == 'perros':
            continue
      print(x)
      
      

 
