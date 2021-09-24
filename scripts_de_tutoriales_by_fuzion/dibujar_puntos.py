

def run():
    print('Hola BIenvenido')
    cantidad = int(input('Oye amborgueso ingresa la cantidad de puntos que quieres: '))
    mensaje = '*'
    on = True    

    if cantidad == 0:            
        cantidad = int(input('ingresa la cantidad de puntos que quieres: '))
    else:
       while on: 
            for n in range(cantidad):
                print(f'{mensaje}')
                if n >= cantidad:
                   

        return on 

if __name__ == '__main__':
    run()
