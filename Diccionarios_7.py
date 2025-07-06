auto={
    "marca":"ford",
    "modelo":"mustang",
    "año":2017,
    "color":"verde"
}
print(auto)

#Acceder al modelo
print(auto["modelo"])

#Modificar
auto["año"]=2023

#Añadir nuevo elemento
auto["color"]="amarillo"
print(auto)

#Eleminar elementos
del auto["modelo"]
print(auto)

auto.pop("marca")
print(auto)