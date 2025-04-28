# Hoy veremos como hacer casting a las variables en Python
# El casting es la conversión de un tipo de dato a otro
# En Python, el casting se puede hacer de la siguiente manera:
# int() - construye un entero a partir de un número entero, 
# un número de coma flotante (por redondeo), 
# o una cadena de caracteres (proporcionando la base)
# float() - construye un número de coma flotante a partir
# de un número entero, un número de coma flotante (por redondeo), 
# o una cadena de caracteres (proporcionando la base)
# str() - construye una cadena de caracteres a partir de una
# amplia variedad de tipos de datos, incluyendo cadenas de 
# caracteres, enteros y números de coma flotante

#podemos hacer casting en una misma línea

cadena = "1234"
entero = 45
flotante = 56.2

# Dos formas de conversión a varable (Casting) El cambio se debe de guardar en una variable

#1
cadenaint = int(cadena)
divi = cadenaint/2
print(divi)

#2
int(cadena)
divi= int(cadena)/2
print(divi)
print()


##############

nombre = "Alan Turing"
edad = 38
notaFinal = 8.50
esEstudiante = False
domicilio = "Av. Talento Tech 1234"
print(type(nombre))         # <class 'str'>, cadena (string)
print(type(edad))           # <class 'int'>, entero (integer)
print(type(notaFinal))      # <class 'float'>, coma flotante (float)
print(type(esEstudiante))   # <class 'bool'>, lógico o booleano (boolean)
print(type(domicilio))      # <class 'str'>, cadena (string)


###############

# Operador de asignación
cantidad = 43       # int (enteros)
precio = 12.45      # float (reales)
nombre = "Adrián"   # string (cadenas)
encendido = True    # bool (lógicos)

# Valores en función del valor ASCII de cada caracter
nombre1 = "Ana"
valorbool = nombre1 > nombre
print(valorbool)
valorbool = nombre1 < nombre
print(valorbool)


saludo = "Hola " + nombre1 + " " + nombre
print(saludo)

# Literales en Python (valores que se pueden asignar a una variable)
# que son los literales en Python?
# Son los valores que se pueden asignar a una variable
# 3 tipos de literales en Python
# 1. Literales numéricos
# 2. Literales de cadena
# 3. Literales booleanos


raiz = 9 ** 0.5
print(raiz) # 3.0
raiz = 9 ** (1/2)
print(raiz) # 3.0
raiz = 125 ** (1/3)
print(raiz) # 5.0
raiz = 27 ** 0.3333333333333333
print(raiz) # 3.0


###########################
# función input() con CASTING
num1 = input("Ingrese un número: ") #El input siempre se toma como STRING
print(type(num1))

numero = float(num1) # Se modifica el string a float
resultado = numero * 2
print(numero,"x 2 =", resultado)

# O se puede hacer el CASTING DIRECTO así --> num1 = int(input("Ingrese un número: "))

###########################

nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
print()
print("El promedio de las tres notas es:",promedio)

######### TAREA
# Crea un programa que solicite al usuario dos números enteros. 
# Realiza las siguientes operaciones: suma, resta, multiplicación, y módulo. 
# Muestra el resultado de cada operación en un formato claro y amigable. 
# Asegúrate de incluir mensajes personalizados que expliquen cada resultado, 
# por ejemplo: "La suma de tus números es: X".

#Calculadora básica


num1 = int(input("Ingresa un número entero: "))
num2 = int(input("Ingresa otro número entero: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
modulo = num1 % num2
print()
print("La suma de tus números es: ", suma)
print("La resta de tus números es: ", resta)
print("La multiplicación de tus números es: ", multiplicacion)
print("El módulo de tus números es: ", modulo)


