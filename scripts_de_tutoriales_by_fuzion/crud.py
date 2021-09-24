clients = 'person1, person2'

def print_clients_list():
    global clients
    return print(f'CLients list: {clients}')


def add_clients():
        global clients
        print_clients_list()
        client_name = input('Write a client name: ').capitalize()
        clients += client_name
        
        print_clients_list() 


def update_clients():
    global clients
    print_clients_list()
    #old_client = str(input('write a name of the list to remplace: ').capitalize)
    old_client = input('write a name of the list to remplace: ').capitalize()
    old_client = str(old_client)
    print(f'Client to be remplace: {old_client}')
    new_client = input('Write a new name of client: ').capitalize()
    new_client =str(new_client)
    print(new_client)
    if old_client in clients:
        clients = clients.replace(old_client, new_client)
        print_clients_list()
    else:
        print(f'The client {old_client} is not in the list :c')

def delete_clients():
    global clients
    print_clients_list()
    client_to_delete = input('write the name to delete in the list: ').capitalize()
    clients = clients.replace(client_to_delete, '')
    print_clients_list() 



def list_clients():
    #global clients
    print_clients_list()


if __name__ == '__main__':
    print('*'*10 + ' Bienvenido elige una opcion ' + '*'*10)
    #run()
    opcion = input('''
            -|A|dd clients.
            -|U|pdate clients.
            -|D|elete client.
            -|L|ist clients.
            -|x|exit
'''
+ '*'*4999999999 ).upper()
    
    if opcion == 'A':
        add_clients()

    elif opcion == 'U':
        update_clients()

    elif opcion == 'D':
        pass
        delete_clients()

    elif opcion == 'L':
        pass
        list_clients()


    elif opcion == 'X':
        pass

        #exit()
    else:
        print('elige una opcion valida')
