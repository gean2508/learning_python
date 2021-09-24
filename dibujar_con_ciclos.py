def run():
    
    eje_x = int(input('Ingresa valor del eje X: '))
    eje_y = int(input('Ingresa valor del eje y: '))
    

    #el cuadrado empieza en eje 0,0 (y,x), dibuja primero abajo, derecha, arriba, izquierda para finalizar.
    for i in range(eje_y):
        print('\n')
        for u in range(eje_x):
            print('*', end='') 


if __name__ == '__main__':
    run()
