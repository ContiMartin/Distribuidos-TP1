# Este cliente es Igual practicamente al cliente 2 pero no guarda los estados.

import socket
# Utilizaremos el módulo Pickle. 
# Este nos permite almacenar casi cualquier objeto Python directamente en un archivo o cadena
# sin necesidad de realizar ninguna conversión. 
# Lo que el módulo pickle realiza en realidad es lo que se llama serialización de objetos, es decir, 
# convertir objetos a y de cadenas de bytes. El objeto que va a ser pickled se serializará en un flujo de bytes, 
# los cuales se pueden escribir en un archivo, por ejemplo, y restaurar en un punto posterior
import pickle

server_address = ("0.0.0.0", 8081)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_address)

keep_working = True

# Basicamente se elimino la opcion de Obtener
COMMAND = {"A": 1}

while keep_working:
    print("Ingrese un comando ([A]cumular, [S]alir)")
    comando = input()

    if comando == "A":
        print("Ingrese un valor a acumular")
        
        #  -----------------------------------
        
        try:
            valor = int(input())
            payload = {"command": COMMAND[comando], "valor": valor}
            
            # Pickle lo que hace es serializar el "valor"
            payload_serialized = pickle.dumps(payload)
            client.sendall(payload_serialized)
            data = client.recv(4096)
            
            # Aca si ya con pickle para que serializa el valor
            result = pickle.loads(data)
            print(f"El valor acumulado es: {result.get('valor')}")
        except ValueError:
            print("Debe ingresar un numero")

    # El salir queda igual
    elif comando == "S":
        keep_working = False
        client.close()
        print("Sesion finalizada")

    # Este queda igual por si ingresa algo no valido..
    else:
        print("El comando ingresado no es valido")


