# tipos_de_datos.py

# Numeros
x, y = 1, 4
z = x

print(x, y, z)

z = 7

print(x, y, z)

# Operaciones
entero = 1
decimal = 9.5

print(entero)
print(decimal)
print(abs(decimal))

suma = entero + 5
decimal *= 2

print(suma)
print(decimal)

# Cadenas
cadena = 'cadena de texto'
cadena2 = cadena

print(cadena)
print(cadena2)

# Listas
lst = [12, 3, 9]
lst.append(10.1)

lst_copia = lst
lst_copia[2] = 20

print(lst, lst_copia)
print(lst_copia.index(20))

lst_copia.insert(2, 'Carlos')
del lst_copia[0]
print(lst_copia)

# Tuplas
tupla = (2, 3, 4, 'car')
print(tupla)

# Rangos
numero_inicio = -5
numero_final = 10
paso = 2
rango = list(range(numero_final))
rango2 = list(range(numero_inicio, numero_final, paso))
print(rango)
print(rango2)
