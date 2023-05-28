import hashlib

def suma():
    suma = 3 + 10
    return suma

print(suma())

print('\n----------Paso de parámetros----------')
def menor_valor(lst):
    return min(lst)

print(menor_valor([6, 2, 9, 7]))

def iniciales(cad, sep=' '): # valor por defecto en el parámetro sep
    return ''.join([x[0].upper() for x in cad.split(sep)])

cadena = iniciales('Devuelve las iniciales de cada palabra separadas por sep')
print(cadena)

print('\n----------Modularización----------')
def extraer_identificadores(cadena_original, sep=' '):
    return cadena_original.split(sep)

def aplicar_hash(l):
    md5s = []
    for c in l:
        m = hashlib.md5(c.encode('utf-8'))
        md5s.append(m.hexdigest())
    return md5s

cadena_original = 'texto<>a<>guardar'
identificadores = extraer_identificadores(cadena_original, sep='<>')
print(identificadores)
id_modificados = aplicar_hash(identificadores)
print(id_modificados)
