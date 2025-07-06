#Metodos fundamentales de listas.

#Append: Añadir un nuevo valor.
#1
# numero=[]
# print(numero)
# num1=7
# numero.append(num1)
# print(numero)
#2
# nombres=[]
# print(nombres)
# nom1=("Ana")
# nom2=("Lucia")
# nom3=("Carlos")
# nombres.append(nom1)
# nombres.append(nom2)
# nombres.append(nom3)
# print(f"Los nombres son, {nombres}")

#insert: Agregar un elemnto en un lugar especifico.
#1
# lista=[1,2,3]
# lista.insert(0,99)
# print(lista)
#2
# colores=["azul","verde"]
# print(colores)
# colores.insert(1,"rojo")
# print(colores)

#extend: Unir listas.
#1
# numeros=[4,5,6]
# print(numeros)
# numeros.extend([1,2,3])
# print(f"La lista de los numeros es, {numeros}")
#2
# letras=["a","b","c"]
# letras.extend(["OK"])
# print(letras)

#remove: Quitar un elemto especifico.
#1
# frutas=["Manzana","Uva","Pera"]
# print(frutas)
# frutas.remove("Uva")
# print(f"De la lista inicial se elimina Uva, {frutas}")
#2
# numeros=[1,2,3,2]
# numeros.remove(2)
# print(f"De la lista iniciala se elimino el numero dos, {numeros}")

#pop: Usar y quitar un elemento.
#1
# lista=[1,2,3,4]
# valor=lista.pop(3)
# print(lista)
# print(valor)
#2
# numeros=["uno","dos","tres"]
# Valor=numeros.pop(0)
# print(numeros)

# clear: Elimina todos los elemntos de una lista.
#1
# lista=[1,2,3,4,5]
# lista.clear()
# print(lista)
#2
# elementos=[]
# ele1=input("Ingrese el primer elemento: ")
# ele2=input("Ingrese el segundo elemento: ")
# ele3=input("Ingrese el tercer elemento: ")
# ele4=input("Ingrese el cuarto elemento: ")
# ele5=input("Ingrese el quinto elemento: ")
# lista=[ele1,ele2,ele3,ele4,ele5]
# print(lista)
# lista.clear()
# print(lista)

#index: Saber en que lugar esta un elemento dentro de una lista. 
#1
# frutas=["manzana","uva","pera"]
# print(frutas)
# print(frutas.index("pera"))
#2
# numeros=[4,5,6,7]
# print(numeros)
# print(numeros.index(6))

#count: Cuenta cuantas veces aparece el valor en x lista.
#1
# lista=[3,1,3,5,3]
# print(lista)
# print(lista.count(3))
#2
# letras=["a","b","a","c","a"]
# print(letras)
# print(letras.count("a"))

#sort: Ordena la lista de menor a mayor (numeros) y alfabeticamente (si son textos).
#1
# numeros=[5,1,4,2]
# numeros.sort()
# print(numeros)
#2
# letras=["z","a","m","b"]
# letras.sort()
# print(letras)

#reverse:Invierte el orden actual de los elementos de una lista (No los ordena solo los gira). 
#1
# numeros=[1,2,3,4,5]
# numeros.reverse()
# print(numeros)
#2
# lista=["Inicio","Medio","Fin"]
# lista.reverse()
# print(lista)

#copy: Crea una copia exacta de la lista, pero independiente (Modificar la copia no afecta la original).
#1
# lista=[1,2,3,4,5]
# nueva_lista=lista.copy()
# nueva_lista.append(6)
# print(lista)
# print(nueva_lista)
#2
# letras=["a","b","c"]
# nueva_lista=letras.copy()
# nueva_lista.append("d")
# print(letras)
# print(nueva_lista)

