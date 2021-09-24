#1._registrar nombres.
import time
clients = 'gean,  '
#def run():
    

def client_add(client_name): 
        global clients 
        print(clients)
        clients += client_name 
        print(clients)
    
def client_update(old_client_name, new_client_name):
        global clients
        #print('Lista de los clientes:')
        #print(clients)
        if old_client_name in clients:
            clients = clients.replace(old_client_name + ', ', new_client_name + ', ')
        else:
            print(f'El cliente {nombre} no se encuentra en a lista, pero puedes agregarlo como uno nuevo...') 
        

    
   
if __name__ == '__main__':
    
    nombre = input('Ingresa tu nombre: ').capitalize()
    opcion = input("""
               -----WELCOME-----
            To:
            -Add client press: 'a' 
            -Update client press: 'u' 
            -Delete client press: 'd'
            -To Exit press: 'x' 
            
            Write your opcion and press enter: """).lower()
    if opcion == 'a':
         client_add(nombre) 
         print('Seleccionaste add')
        
    elif opcion == 'u':
        #global clients
        #print(clients)
        #print('Para actualizar un cliente, debes ingresar su nombre actual  por uno nuevo.')
        #nombre = input('Ingresa el nombre del cliente que va a ser actulizado: ')
        new_client_name =  input('Ingresa el nuevo nombre del cliente: ')
        client_update(nombre, new_client_name)
        print('Seleccionaste update.....trabajando')        
    elif opcion == 'd':
        print('Seleccionaste delete...trabajando')
         
    elif opcion == 'x':
        print('Seleccionaste exit...trabajando')
    else:
         print('Ingresa una opcion valida c:')

    #run()


