from collections import defaultdict
import socket

from structures import *

server_address = (('0.0.0.0', 8081))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_address)
server.listen()

acumulador = defaultdict(lambda: 0)
 
payload=payload_X()

while True:
    print('Server disponible!')
    connection, client_address = server.accept()    

    while True:
        print('-----------------')
        print(acumulador)
        print('-----------------')

        print(client_address)
        
        data = connection.recv_into(payload)

        if not data: break
        
        if payload.operation == 1:
            acumulador[payload.token] += payload.data

        elif payload.operation == 2:
            payload.data = acumulador[payload.token]
            connection.sendall(payload)
            
        else:
            print(f'El cliente {payload.token} solicito el comando {payload.operacion} con el valor {payload.data}')
            break
        

    connection.close()
    print('cliente desconectado \n')
