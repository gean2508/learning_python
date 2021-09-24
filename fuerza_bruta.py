#algoritmo de busueda exhaustiva o fuerza bruta
#en este caso es apicado a encontrar la raiz cuadrada de un numero ingresado por el client
def main():
    print('----------------------- Hola bienvenido ------------------------')    
    objetivo = int(input('Ingresa la canitidad: '))
    #inicializamos una variable respuesta en cero :B
    respuesta = 0
    while respuesta**2 < objetivo:
        respuesta +=1
      #  print(f'soy respuesta despues de entrarar en el while {respuesta}')
    
    if respuesta**2 == objetivo:
        print(f'La raiz de {objetivo} es {respuesta} :] BYe')
       # print(f'soy respuesta encontrando la raiz{respuesta}')
    else:
        print('no hay raiz :c')



if __name__ == "__main__":
    main()
