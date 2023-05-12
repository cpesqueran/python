# tipos_de_datos.py

# Numeros
print('----------Numeros----------')
x, y = 1, 4 # Asignaciones múltiples
z = x

print(x, y, z)

z = 7

print(x, y, z)

# Operaciones
print('\n----------Operaciones----------')
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
print('\n----------Cadenas----------')
cadena = 'Cadena de texto con comillas simples.'
cadena2 = "Cadena de texto con comillas dobles y salto.\n"
cadena3 = "Esto es una frase 'corta' usando comillas con salto.\n"
cadena4 = 'Esto es una frase "corta" usando comillas con salto.\n'
cadena5 = '''Esto es una frase usando comillas 'simples' y "dobles" en la \
frase.\n'''

parrafo1 = 'Frase simple\n \
    convertida en parrafo.\n'
parrafo2 = '''Esto es un parrafo sin poner ningun tipo de salto de linea entre
cada una de las frases
que la componen.\n''' 

print(cadena)
print(cadena2)
print(cadena3)
print(cadena4)
print(cadena5)
print(parrafo1)
print(parrafo2)

i = 6
print(f'Esto es el valor de {i}\n')

# Listas
print('----------Listas----------')
lst = [12, 3, 9]
lst.append(10.1)

lst_copia = lst
lst_copia[2] = 20

print(lst, lst_copia)
print(lst_copia.index(20))
print(len(lst_copia))

lst_copia.insert(2, 'Carlos')
del lst_copia[0]
print(lst_copia)

# Tuplas
print('\n----------Tuplas----------')
tupla = (2, 3, 4, 'car')
print(f'{tupla}\n')

# Rangos
print('----------Rangos----------')
numero_inicio = -5
numero_final = 10
paso = 2
rango = list(range(numero_final))
rango2 = list(range(numero_inicio, numero_final, paso))
print(rango)
print(rango2)
