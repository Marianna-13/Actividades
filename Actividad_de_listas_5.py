#Actividad de listas
lista1=[1,2,3,4,5]
lista2=[6,7,8,9,10]

lista1.append(100)
lista1.append("Hola Mundo")

lista2.append(300)
lista2.append("Hola Y Adios")

lista3=lista1.copy()
lista3.remove("Hola Mundo")

lista4=lista2.copy()
lista4.remove("Hola Y Adios")
lista4.remove(300)

lista5=[]
lista5.extend(lista4)
lista5.extend(lista3)

print("LiSTA 1",lista1)
print("LiSTA 2",lista2)
print("LiSTA 3",lista3)
print("LiSTA 4",lista4)
print("LiSTA 5",lista5)
