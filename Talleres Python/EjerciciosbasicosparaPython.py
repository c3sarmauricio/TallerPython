#EJERCICIOS BÁSICOS PARA PYTHON

#Ejercicio 1

# numeroalumnos = 0
# promedio = 0
# edad = 0
# sumaedades = 0
# continuar = "SI"
# while continuar == "SI":
#     edad = int(input("Ingrese la Edad:\n"))
#     if edad > 18 & promedio != 0:
#         print("El promedio de edades sin incluir la edad anterior es: ",promedio)
#     numeroalumnos += 1
#     sumaedades = sumaedades + edad
#     promedio = int(sumaedades / numeroalumnos)
#     continuar = input("¿Digite SI para continuar?\n")
# print("El Promedio Final de Edades Ingresadas es:", promedio)


#Ejercicio 2

# cantidad = 0
# suma = 0
# for i in range(10):
#     cantidad = int(input("Ingrese una Cantidad\n"))
#     suma = suma + cantidad
# print("La suma total de los 10 números ingresados es: ", suma)


#Ejercicio 3

# suma = 0.0
# contador = 0.0
# promedio = 0.0
# estatura = input("Ingrese la Estatura:\n")
# if estatura == "":
#     estatura = 0.0
# while float(estatura) > 0.0:
#     contador += 1.0
#     suma = float(estatura) + suma
#     promedio = suma / contador
#     estatura = input("Ingrese la Estatura:\n")
#     if estatura == "":
#         estatura = 0.0
# print("Se Ingresaron ",contador," datos, el promedio de estatura es: ",promedio)


#Ejercicio 4

# cantidad = 0
# menor = 0
# igual = 0
# mayor = 0
# continuar = "SI"

# while continuar == "SI":
#     cantidad = int(input("Ingrese una cantidad\n"))
#     if cantidad < 0:
#         menor = menor + 1
#     if cantidad == 0:
#         igual = igual + 1
#     if cantidad > 0:
#         mayor = mayor + 1
#     continuar = input("Digite SI para continuar:\n")
# print("Se ingresaron ", menor, " datos menores que 0." )
# print("Se ingresaron " , igual, " datos iguales a 0.")
# print("Se ingresaron ",  mayor, " datos mayores que 0." )


#Ejercicio 5

            #solución 1

num = 1
productopares = 1
productoimpares = 1
pares = []
impares = []
while num <= 100:
    if num % 2 == 0:
        pares.append(num)
        productopares *= num
    else:
        impares.append(num)
        productoimpares *= num
    num += 1
print("Lista de Pares:\n",pares)
print("La Multiplicación de todos los números Pares es:\n",productopares)
print("Lista de Impares:\n",impares)
print("La Multiplicación de todos los números Impares es:\n",productoimpares)


#Ejercicio 6

# a = 0
# b = 1
# i = 0
# n = int(input("Ingrese la Cantidad de números Fibonacci que desea imprimir:\n"))
# print(a)
# print(b)
# while i < n:
#     s = a + b
#     a = b
#     b = s
#     print(s)
#     i += 1

