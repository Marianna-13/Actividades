#Ejercicios de practica

#1 Calculadora de promedio
# lista=[]
# nota1=float(input("Ingresa la primera calificacion: "))
# nota2=float(input("Ingresa la segunda calificacion: "))
# nota3=float(input("Ingresa la tercera calificacion: "))
# operacion=(nota1+nota2+nota3)/3
# lista.append(nota1)
# lista.append(nota2)
# lista.append(nota3)
# print(f"El promedio y la lista son {operacion}, {lista}")


#2 Analiza precios
# productos={
#     "manzana":2.000,
#     "huevos":1.100,
#     "queso":5.000
# }
# print(productos)
# porcentaje=float(input("Porcentaje de aumento (%): "))
# productos["manzana"]+=productos["manzana"]*(porcentaje/100)
# productos["huevos"]+=productos["huevos"]*(porcentaje/160)
# productos["queso"]+=productos["queso"]*(porcentaje/100)
# print(productos)


#3 Conversor de temperaturas
# c1=float(input("Ingresa la primera temperatura: "))
# c2=float(input("Ingresa la segunda temperatura: "))
# c3=float(input("Ingresa la tercera temperatura: "))
# c4=float(input("Ingresa la cuarta temperatura: "))
# c5=float(input("Ingresa la quinta temperatura: "))
# celcius=(c1,c2,c3,c4,c5)

# f1=c1*9/5+32
# f2=c2*9/5+32
# f3=c3*9/5+32
# f4=c4*9/5+32
# f5=c5*9/5+32
# fahreheit=(f1,f2,f3,f4,f5)

# print(f"La temperatur en celcius es {celcius}")
# print(f"La temperatura en fahreheit es {fahreheit}")


#4 Edad promedio
# edades=[int(input("edad 1: ")), int(input("edad 2: ")), int(input("edad 3: ")), int(input("edad 4: ")), int(input("edad 5: "))]
# promedio=sum(edades)/len(edades)
# print(f"Mayor: {max(edades)}, Menor: {min(edades)}, Promedio: {promedio}")


#5 Diccionario de frutas
# frutas={
#     "durazno":4.900,
#     "fresa":11.400,
#     "piña":1.980
# }
# kilos1=float(input("Cuantos kilos de fruta necesita?: "))
# kilos2=float(input("Cuantos kilos de fruta necesita?: "))
# kilos3=float(input("Cuantos kilos de fruta necesita?: "))
# suma=(kilos1*(frutas["durazno"]))+(kilos2*(frutas["fresa"]))+(kilos3*(frutas["piña"]))
# print(f"El total a pagar es {suma}")

#6 Suma de tuplas
# numeros=(1,2,3,4,5)
# suma=sum(numeros)
# print(f"La suma de los elementos de la tupla es: {suma}")


#7 Inventario con lista de dicionarios
# inventario=[]
# ##Producto 1
# nombre1=input("Ingresa el nombre del primer producto: ")
# cantidad1=int(input("Que cantidad desea?: "))
# precio1=float(input("Cual es el precio?: "))
# producto1={
#     "Nombre":nombre1,
#     "Cantidad":cantidad1,
#     "Precio":precio1
# }
# inventario.append(producto1)
# ##Producto 2
# nombre2=input("Ingresa el nombre del segundo producto: ")
# cantidad2=int(input("Que cantidad desea?: "))
# precio2=float(input("Cual es el precio?: "))
# producto2={
#     "Nombre":nombre2,
#     "Cantidad":cantidad2,
#     "Precio":precio2
# }
# inventario.append(producto2)
# ##Producto 3
# nombre3=input("Ingresa el nombre del tercer producto: ")
# cantidad3=int(input("Que cantidad desea?: "))
# precio3=float(input("Cual es el precio?: "))
# producto3={
#     "Nombre":nombre3,
#     "Cantidad":cantidad3,
#     "Precio":precio3
# }
# inventario.append(producto3)
# total=(cantidad1*precio1)+(cantidad2*precio2)+(cantidad3*precio3)
# print(f"El total del inventario fue {total}, y la lista es {inventario}")


#8 Modificar una lista de precios
# precios=[10.000,15.000,33.000,43.000,65.000]
# descuento=float(input("Ingresa el descuento %: "))
# precio1=precios[0]-(precios[0]*descuento/100)
# precio2=precios[1]-(precios[1]*descuento/100)
# precio3=precios[2]-(precios[2]*descuento/100)
# precio4=precios[3]-(precios[3]*descuento/100)
# precio5=precios[4]-(precios[4]*descuento/100)
# precios_con_descuento=[precio1,precio2,precio3,precio4,precio5]
# print(f"Los precios originales son {precios}")
# print(f"Los precios con descuento son {precios_con_descuento}")

#9 Notas con tuplas
# notas1=float(input("Ingresa la primera notas: "))
# notas2=float(input("Ingresa la segunda notas: "))
# notas3=float(input("Ingresa la tercera notas: "))
# notas4=float(input("Ingresa la cuarta notas: "))
# notas=[notas1,notas2,notas3,notas4]
# tupla=tuple(notas)
# print(f"Mayor: {max(notas)}, Menor: {min(notas)} {tupla}")


#10 Diccionarios de conversores
# conversores={
#     "km":1000,
#     "m":1,
#     "cm":0.01
# }
# print("Las unidades disponibles son km, m, cm")
# unidad=input("Escibe la unidad que estas usando: ")
# cantidad=float(input("Ingresa la cantidad: "))
# factor=conversores[unidad]
# metros=cantidad*factor
# print(f"{cantidad}, {unidad} equivale a {metros} metros")


#11 Lista de productos mas IVA
# precio1=float(input("Ingresa el primer precio: "))
# precio2=float(input("Ingresa el segundo precio: "))
# precio3=float(input("Ingresa el tercer precio: "))
# precio4=float(input("Ingresa el cuarto precio: "))
# precios=[precio1,precio2,precio3,precio4]

# precio1_IVA=precio1+(precio1*0.19)
# precio2_IVA=precio2+(precio2*0.19)
# precio3_IVA=precio3+(precio3*0.19)
# precio4_IVA=precio4+(precio4*0.19)
# precios_iva=[precio1_IVA,precio2_IVA,precio3_IVA,precio4_IVA]

# print(f"Los precios originales son {precios}")
# print(f"Los precios con el IVA son {precios_iva}")


#12 Tupla de operaciones matematicas
# num1=int(input("Ingresa el pimer numero: "))
# num2=int(input("Ingresa el segundo numero: "))
# suma=num1+num2
# resta=num1-num2
# multiplicacion=num1*num2
# division=num1/num2
# resultados=(suma,resta,multiplicacion,division)
# print(f"Los resultados de las operaciones son {resultados}")


#13 Diccionario de estudiantes
# nombre1=input("Nombre del primer estudiante: ")
# nota1=float(input("Nota de " +nombre1+ ": " ))

# nombre2=input("Nombre del segundo estudiante: ")
# nota2=float(input("Nota de " +nombre2+ ": " ))

# nombre3=input("Nombre del primer estudiante: ")
# nota3=float(input("Nota de " +nombre3+ ": " ))

# estudiantes={
#     nombre1:nota1,
#     nombre2:nota2,
#     nombre3:nota3
# }
# promedio=(nota1+nota2+nota3)/3
# print(f"Los estudiantes {estudiantes} tubieron un promedio de {promedio}")


#14 Lista de salarios
# salario1=float(input("Ingresa el primer salario: "))
# salario2=float(input("Ingresa el segundo salario: "))
# salario3=float(input("Ingresa el tercer salario: "))
# salario4=float(input("Ingresa el cuarto salario: "))
# salario5=float(input("Ingresa el quito salario: "))
# salarios=[salario1,salario2,salario3,salario4,salario5]

# aumento1=salario1+(salario1*0.10)
# aumento2=salario2+(salario2*0.10)
# aumento3=salario3+(salario3*0.10)
# aumento4=salario4+(salario4*0.10)
# aumento5=salario5+(salario5*0.10)
# aumentos=[aumento1,aumento2,aumento3,aumento4,aumento5]

# print(f"Los salarios originales son {salarios}")
# print(f"Los salarios con el aumento son {aumentos}")


#15 Diccionario de impuestos
# productos={
#     "mango":3.800,
#     "lulo":4.800,
#     "limon":1.500
# }
# impuesto=float(input("Ingresa el porcentaje de impuesto: "))
# tasa=impuesto/100

# mango1=productos["mango"]+(productos["mango"]*tasa)
# lulo1=productos["lulo"]+(productos["lulo"]*tasa)
# limon1=productos["limon"]+(productos["limon"]*tasa)

# precios_finales={
#     "mango":mango1,
#     "lulo":lulo1,
#     "limon":limon1
# }
# print(f"Los precios sin impuestos son {productos}")
# print(f"Los precios con los impuestos {precios_finales}")


#16 Analisis de listas de edades
# edad1=int(input("Ingresa la primera edad: "))
# edad2=int(input("Ingresa la segunda edad: "))
# edad3=int(input("Ingresa la tercera edad: "))
# edad4=int(input("Ingresa la cuarta edad: "))
# edad5=int(input("Ingresa la quinta edad: "))
# edad6=int(input("Ingresa la sexta edad: "))
# lista_edades=[edad1,edad2,edad3,edad4,edad5,edad6]

# mayores=(edad1>=18)+(edad2>=18)+(edad3>=18)+(edad4>=18)+(edad5>=18)+(edad6>=18)
# menores=5-mayores

# print(f"Las edades son {lista_edades}")
# print(f"Los mayores de edad son {mayores}, y los menores de edad son {menores}")


#17 Tupla de conversiones de edad
# dolares=float(input("Ingresa la canntidad en dolares: "))
# tasa_E=0.85
# tasa_P=17.0
# tasa_Y=155.0

# euros=dolares*tasa_E
# pesos=dolares*tasa_P
# yenes=dolares*tasa_Y
# conversiones=(euros,pesos,yenes)

# print(f"La conversion de los dolares en Euros, Pesos y Yenes es {conversiones}")


#18 Diccionario de ventas
# nombre1=input("Nombre del primer producto: ")
# cantidad1=float(input("Cantidad de " +nombre1+ ": " ))

# nombre2=input("Nombre del segundo producto: ")
# cantidad2=float(input("Cantidad de " +nombre2+ ": " ))

# nombre3=input("Nombre del primer producto: ")
# cantidad3=float(input("Cantidad de " +nombre3+ ": " ))

# ventas={
#      nombre1:cantidad1,
#      nombre2:cantidad2,
#      nombre3:cantidad3
# }
# total=cantidad1+cantidad2+cantidad3

# print(f"Las ventas fueron {ventas}, y el total de las unidades vendidas es {total}")


#19 LIsta de temperaturas estremas
# temperaturas=[5,12,24,33,49,52,3,11,1,89]

# mayores_tem={
# temperaturas[2],
# temperaturas[3],
# temperaturas[4],
# temperaturas[5],
# temperaturas[9]
# }
# menores_tem={
#     temperaturas[0],
#     temperaturas[1],
#     temperaturas[6],
#     temperaturas[7],
#     temperaturas[8]
# }
# print(f"Las temperaturas son {temperaturas}")
# print(f"Las temperaturas mayores fueron {mayores_tem}, y las menores fueron {menores_tem}")


#20 Actualizar precios con metodos de listas
precios=[1.000,45.000,110.000,34.000,64.000]
print(f"Los precios actuales son {precios}")

eliminar=float(input("Ingrese el precio que desea eliminar: "))
precios.remove(eliminar)

agregar=float(input("Ingrese el precio que desea agregar: "))
precios.append(agregar)

precios.sort()

print(f"Lista de precios nueva y ordenada {precios}")