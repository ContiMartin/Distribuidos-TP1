import socket

# Utilizaremos el módulo Pickle. 
# Este nos permite almacenar casi cualquier objeto Python directamente en un archivo o cadena
# sin necesidad de realizar ninguna conversión. 
# Lo que el módulo pickle realiza en realidad es lo que se llama serialización de objetos, es decir, 
# convertir objetos a y de cadenas de bytes. El objeto que va a ser pickled se serializará en un flujo de bytes, 
# los cuales se pueden escribir en un archivo, por ejemplo, y restaurar en un punto posterior

import pickle

# De esta inicializacion no cambia nada
server_address = ("0.0.0.0", 8081)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_address)
server.listen()

while True:
    print("Server disponible!")
    connection, client_address = server.accept()
    
    # Esto es nuevo, aca
    client = ":".join(list(map(str, client_address)))
    print(f"Cliente {client}")

    while True:

        # A data le pongo lo que viene de la conexion
        data = connection.recv(4096)

        # Aca se produce la magia de Pickle para que interprete que se quiere hacer
        payload = pickle.loads(data)
        
        comando = payload.get("command")


        # Si data no es nada, se va y sale.
        if not data: break

        if comando == 1:
            valor = payload.get("valor")
            response = {"valor": valor}
            response_serialized = pickle.dumps(response)
            connection.sendall(response_serialized)

        else:
            print(f"El cliente solicito el comando {comando} con el valor {payload.get('valor')}")
            break

    connection.close()
    print("cliente desconectado \n")