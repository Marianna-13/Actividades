#EJERCICIOS CON CONDICIONALES Y OPERACIONES MATEMATICAS.

#1 Verifica si un numero es positivo negativo o cero.
# numero1=float(input("Ingrese un numero: "))
# if numero1 > 0:
#     print("Positivo")
# elif numero1 < 0:
#     print("Negativo")
# else:
#     print("Cero")


#2 Calcula si un numero es mayor o menor.
# num1=int(input("Ingrese el pirmer numero: "))
# num2=int(input("Ingrese el segundo numero: "))
# if num1 > num2:
#     print(f"El numero {num1} es mayor, y el {num2} es menor")
# elif num1 < num2:
#     print(f"El numero {num1} es menor, y el {num2} es mayor")


#3 Determina si un numero es par o impar.
# numero=int(input("Ingresa un numero: "))
# if numero % 2 == 0:
#     print("El numero es par ")
# else:
#     print("El numero es impar")


#4 Dado un numero, verifica si esta entre 10 y 20.
# numero=int(input("Ingrese un numero: "))
# if numero >= 10 and numero <=20:
#     print("El numero SI esta entre 10 y 20")
# else:
#     print("El numero NO esta entre 10 y 20")


#5 Dados tres numeros, encuentra el mayor usando condicionales.
# num1=int(input("Ingrese el primer numero: "))
# num2=int(input("Ingrese el segundo numero: "))
# num3=int(input("Ingrese el tercer numero: "))
# if num1 >= num2 and num1 >= num3:
#     mayor=num1
# elif num2 >= num1 and num2 >= num3:
#     mayor=num2
# else:
#     mayor=num3
# print("El numero mayor es ",mayor)


#6 Calcula el precio y el final con un 10% de descuento si el total es mayor a $100.
# total=float(input("Ingrese el precio final de su compra: "))
# if total > 100:
#     descuento = total*0.10
#     precio_final=total-descuento
#     print("A su compra SI se  le agrego un 10% de descuento")
# else:
#     print("A su compra NO se le agrego descuento")


#7 Verifica si una persona puede votar (mayor o igual a 18 años).
edad=int(input("Ingrese su edad: "))
if edad >= 18:
    print("Si puede votar")
else:
    print("No puede votar ya que es menor de 18")