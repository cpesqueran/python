tipo = 'coche'

if tipo == 'coche':
    ruedas = 4
elif tipo == 'bicicleta':
    ruedas = 2
elif tipo == 'camion':
    ruedas = 6
else:
    ruedas = -1

print(ruedas)

i = 1
while i <= 5:
    print(f'Contador {i}')
    i += 1

en_bucle = True
while en_bucle:
    x = int(input('Introduzca un número ( 0 para terminar): '))
    if x < 0:
        print(f'El número {x} es negativo.')
    elif x > 0:
        print(f'El número {x} es positivo.')
    elif x == 0:
        en_bucle = False
else:
    print('Salimos!')

lista = [4, 7, 12, 20, 27]
print(f'Lista: {lista}')
for i in lista:
    print(f'Item {i} de la lista.')
        