# Oscar Flores NC = 1389

# ------------------------------------------
# 1. Variables 
# ------------------------------------------
# Ejemplo 1: Declaración de variables numéricas y de texto
edad = 25
nombre = "Ana"
precio = 19.99

print("--- 1. Variables: Ejemplo 1 ---")
print("Nombre:", nombre)
print("Edad:", edad)
print("Precio:", precio)
print()

# Ejemplo 2: Asignación de variables con cambio de tipo (Casting)
x = str(3)    # 'x' será '3'
y = int(3)    # 'y' será 3
z = float(3)  # 'z' será 3.0

print("--- 1. Variables: Ejemplo 2 ---")
print("x (str):", x, type(x))
print("y (int):", y, type(y))
print("z (float):", z, type(z))
print()

# Ejemplo 3: Sensibilidad a mayúsculas/minúsculas (Case-Sensitive)
a = 10
A = "Hola"

print("--- 1. Variables: Ejemplo 3 ---")
print("a (minúscula):", a)
print("A (mayúscula):", A)
print()


# ------------------------------------------
# 2. Asignación Múltiple 
# ------------------------------------------

# Ejemplo 1: Asignar muchos valores a múltiples variables
fruta1, fruta2, fruta3 = "Manzana", "Plátano", "Cereza"

print("--- 2. Asignación Múltiple: Ejemplo 1 ---")
print("Fruta 1:", fruta1)
print("Fruta 2:", fruta2)
print("Fruta 3:", fruta3)
print()

# Ejemplo 2: Un mismo valor a múltiples variables
x = y = z = "Naranja"

print("--- 2. Asignación Múltiple: Ejemplo 2 ---")
print("x:", x)
print("y:", y)
print("z:", z)
print()

# Ejemplo 3: Desempaquetado de una lista 
colores = ["Rojo", "Verde", "Azul"]
c1, c2, c3 = colores

print("--- 2. Asignación Múltiple: Ejemplo 3 ---")
print("Color 1:", c1)
print("Color 2:", c2)
print("Color 3:", c3)
print()


# ------------------------------------------
# 3. Tipos de Datos (python_datatypes.asp)
# ------------------------------------------

# Ejemplo 1: Tipos básicos 
texto = "Hola Mundo"
entero = 42
decimal = 3.1416
booleano = True

print("--- 3. Tipos de Datos: Ejemplo 1 ---")
print(texto, "-> Tipo:", type(texto))
print(entero, "-> Tipo:", type(entero))
print(decimal, "-> Tipo:", type(decimal))
print(booleano, "-> Tipo:", type(booleano))
print()

# Ejemplo 2: Tipos de secuencias 
lista = ["manzana", "banana", "cereza"]
tupla = ("manzana", "banana", "cereza")
rango = range(5)

print("--- 3. Tipos de Datos: Ejemplo 2 ---")
print("Lista:", lista, "->", type(lista))
print("Tupla:", tupla, "->", type(tupla))
print("Rango:", list(rango), "->", type(rango))
print()

# Ejemplo 3: Tipos de mapeo y conjuntos 
diccionario = {"nombre": "Juan", "edad": 30}
conjunto = {"manzana", "banana", "cereza"}

print("--- 3. Tipos de Datos: Ejemplo 3 ---")
print("Diccionario:", diccionario, "->", type(diccionario))
print("Conjunto (Set):", conjunto, "->", type(conjunto))
print()


# ------------------------------------------
# 4. Operadores Aritméticos )
# ------------------------------------------

# Ejemplo 1: Suma, Resta y Multiplicación
a = 15
b = 4

print("--- 4. Operadores Aritméticos: Ejemplo 1 ---")
print(f"Suma: {a} + {b} =", a + b)
print(f"Resta: {a} - {b} =", a - b)
print(f"Multiplicación: {a} * {b} =", a * b)
print()

# Ejemplo 2: División normal y División entera
num1 = 17
num2 = 5

print("--- 4. Operadores Aritméticos: Ejemplo 2 ---")
print(f"División exacto: {num1} / {num2} =", num1 / num2)
print(f"División entera: {num1} // {num2} =", num1 // num2)
print()

# Ejemplo 3: Módulo y Potenciación
base = 3
exponente = 4
dividendo = 10
divisor = 3

print("--- 4. Operadores Aritméticos: Ejemplo 3 ---")
print(f"Módulo (resto): {dividendo} % {divisor} =", dividendo % divisor)
print(f"Exponente: {base} ** {exponente} =", base ** exponente)
print()


# ------------------------------------------
# 5. Operadores de Comparación 
# ------------------------------------------

# Ejemplo 1: Igualdad (==) y Desigualdad (!=)
n1 = 20
n2 = 20
n3 = 30

print("--- 5. Operadores de Comparación: Ejemplo 1 ---")
print(f"¿{n1} == {n2}?:", n1 == n2)
print(f"¿{n1} != {n3}?:", n1 != n3)
print()

# Ejemplo 2: Mayor que (>) y Menor que (<)
p1 = 50
p2 = 100

print("--- 5. Operadores de Comparación: Ejemplo 2 ---")
print(f"¿{p1} > {p2}?:", p1 > p2)
print(f"¿{p1} < {p2}?:", p1 < p2)
print()

# Ejemplo 3: Mayor o igual que (>=) y Menor o igual que (<=)
val1 = 15
val2 = 15

print("--- 5. Operadores de Comparación: Ejemplo 3 ---")
print(f"¿{val1} >= {val2}?:", val1 >= val2)
print(f"¿{val1} <= 10?:", val1 <= 10)
print()


# ------------------------------------------
# 6. Operadores Lógicos 
# ------------------------------------------

# Ejemplo 1: Operador AND 
edad = 22
tiene_licencia = True

print("--- 6. Operadores Lógicos: Ejemplo 1 (AND) ---")
print("¿Puede conducir?:", edad >= 18 and tiene_licencia)
print()

# Ejemplo 2: Operador OR 
es_fin_de_semana = False
es_feriado = True

print("--- 6. Operadores Lógicos: Ejemplo 2 (OR) ---")
print("¿Es día de descanso?:", es_fin_de_semana or es_feriado)
print()

# Ejemplo 3: Operador NOT 
esta_lloviendo = False

print("--- 6. Operadores Lógicos: Ejemplo 3 (NOT) ---")
print("¿Está lloviendo?:", esta_lloviendo)
print("¿Debo salir sin paraguas (not esta_lloviendo)?:", not esta_lloviendo)
print()
print("Programa reealizado por Oscar Flores NC = 1389")