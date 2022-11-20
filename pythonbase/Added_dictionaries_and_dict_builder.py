Cyberspunk = {
    
    "Runner":{
     "Tipo": "Informatico",
     "Unidad": "SAOKO"},
    "Dead metal":{
        "Tipo":"Asalto",
        "Unidad":"Inito"
    }
}
print(Cyberspunk)

#Tambem podemos usar otro tipo de sintax para chegar no mesmo resultado.

Runner ={
    "Tipo":"Informatico",
    "Unidad":"SAOKO"
}

Dead_metal= {
    "Tipo":"Asalto",
    "Unidad":"Inito"
}

Cyberspunk ={
    "Runners": Runner,
    "Dead Metal": Dead_metal
}

print(Cyberspunk)

#Fazer diccionarios com constructor dict

EquiposH = dict(Nombre="EscuadronPF",Armamento = "Quinque", Grupo = "B")


print("Equipos de control", EquiposH)