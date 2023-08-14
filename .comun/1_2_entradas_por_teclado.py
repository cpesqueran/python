#1_2_entradas_por_teclado.py

print('Como te llamas?')
cadena = input()
print(f'Me llamo {cadena}')

print('Como te llamas (con end)?: ', end='')
cadena = input()
print(f'Me llamo {cadena}')

cadena = input('Como te llamas?: ')
print(f'Me llamo {cadena}')

numero = float(input('Intr. EUROS: '))
print(f'Son {numero * 166.386} pesetas.')
