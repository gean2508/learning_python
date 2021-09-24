#pedir una palabra al user y verificar si es o no palindromo




palabra = input('Ingresa una palabra  verfica si es un palindromo: ')

palabra = palabra.strip()
palabra = palabra.lower()


def verificar(palabra):
    #remplazamos todos los espacios con strings vacios
    palabra = palabra.replace(' ', '')
    if palabra[::] == palabra [::-1]:
         return print(f'{palabra} si es un palindromo')
    else:
         return print(f'{palabra} no es un palindromo')
                

verificar(palabra)












