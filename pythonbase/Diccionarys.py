# Agora vamos ver o que são os diccionarios 


#Os diccionarios vai nos permiten criar una llave para accessar os valores que digitamos na izquerda exemplo;
#Nombres = Key, Caty = Valor que digitamos y con la key accesamos a ele
diccionario1 = {
    "Nombres": "Caty",
    "Raza": "Angora",
    "Edad": 2
        
}
# !!print(diccionario1)!!
#!! print(diccionario1['Raza'])!! #Aqui a gente pode usar os corchetes cuadrados para acceder aqueles datos tambem temos outra alternativa --->

# !! print(diccionario1.get('Nombres')) !! #Usamos el metodo.get para mostrar tambien valores de key especificos

# Ago vamos ver como fazer as modificações a esses valores

diccionario1["Nombres"] = 'Dadycat' #A syntax é muito facil de captar eu acho que você da conta rsrs

#Agreguemos valores com a seguinte sintaxys...
#Pode ver como agregamos valores semelhante ao jeito de mudar valores, quando esse valores não existen ele vai simplemente cria um novo
diccionario1['Ronronea?'] = 'SI'

# !!print(diccionario1)!!

#Como eliminar valores? --->

# !diccionario1.pop('Ronronea?')!  #Ja tinhamos visto esse atributo anteriormente. Si colocamos um valor especifico ele vai apagar essa key e seu valor tbm

#Um anhadido é o atributo ! popitem() ! com ele você consegue eliminar o ultimo valor anhadido no diccionario blz?

#Eliminar elementos (Outro jeito) 

# !!copiadiccionario1 = diccionario1.copy()!!! #Copiei o diccionario

copiadiccionario1 = dict(diccionario1) #Ai agregamos esse atributo dict que é outro jeito de fazer uma copia do nosso diccionario 

del diccionario1 ['Edad'] #Eliminei um valor 
 
print(diccionario1,copiadiccionario1 ) #imprimi a modificação e tambem a copia

#Para vaziar todos os valores de um diccionario a gente pode usar o atributo ".clear"

diccionario1.clear()