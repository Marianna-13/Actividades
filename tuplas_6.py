#Tupla a lista
# tupla=(1,2,3,4,5)
# lista=list(tupla)
# print(lista)

#Lista a tupla
# lista=[6,7,8,9,10]
# tupla=tuple(lista)
# print(tupla)

#Ejercicio 1: Lista de frutas
# frutas=("Manzana","Pera")
# lista=list(frutas)
# print(frutas)

# nueva_fruta=input("Ingresa otra fruta: ")
# lista.append(nueva_fruta)
# lista=tuple(lista)

# print(f"La primera lista es {frutas}, despues se le agrega otra fruta {lista}")


#Ejercicio 2: Califiaciones de estudiante
# tupla=(4.2,3.8)
# lista=list(tupla)
# print(tupla)

# nota3=float(input("Ingresa la tercera nota: "))
# lista.append(nota3)

# lista=tuple(lista)

# print(f"Las primeras calificaciones son {tupla}, la tercera calificacion ingresada es {lista}")


#Ejercicio 3: Datos personales
# tupla=("Ana","Gomez")
# lista=list(tupla)

# numero=int(input("Ingrese su numero de documento: "))
# lista.append(numero)

# lista=tuple(lista)

# print(f"El nombre y el numero de documento son {tupla}, {lista}")



#-----------------------Ejercicios practicos-----------------
#Ejercicio 1
# numeros=(1,2,3,4,5)
# print(numeros)

#Ejercico 2
# print(numeros[1])

#Ejercicio 3
# longitud=len(numeros)
# print(longitud)

#Ejercicio 4
# print(numeros.index(5))

#Ejercicio 5
# print(numeros.count(2))

#Ejercicio 6
# tupla=("Pato",13,7.17)
# print(tupla)

#Ejercicio 7
tupla=("Pato","Cerdo",(10,20,30), "Araña")
valor_interno=tupla[2][0]
valor_externo=tupla[1]
print(f"El primer valor de la lista interna es {valor_interno}")
print(f"El segundo animal de la lista externa es {valor_externo}")