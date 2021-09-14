import socket
import pickle

cant_buff = 1024

class FSStub:

    def __init__(self, canal):
        self._channel = canal

    def ListFiles(self, path): 
        # armo el datos con path y el numero de operacion para el servidor 
        datos = {"path": path, "operacion": 1}
        
        # Con pickle encapsulamos o serializamos lo datos
        datos_serializados = pickle.dumps(datos)
        
        # hago la llamada con los datos serializados
        self._channel.sendall(datos_serializados)
        data = self._channel.recv(4096)
        
        # Desearializo los datos y retorno
        data_deserialized = pickle.loads(data)
        return data_deserialized.get("paths")


    def openFile(self, path):
        # armo el datos con path y el numero de operacion para el servidor
        datos = {"path": path, "operacion": 2}
        
        # Con pickle encapsulamos o serializamos lo datos
        datos_serializados = pickle.dumps(datos)

        # hago la llamada con los datos serializados
        self._channel.sendall(datos_serializados)
        data = self._channel.recv(4096)
        
        # Desearializo los datos y retorno
        data_deserialized = pickle.loads(data)
        return data_deserialized.get("open")

    def readFile(self, path, offset, cant_bytes):
        # armo el datos con path, el numero de operacion para el servidor
        # el offset y la cantidad de bytes
        datos = {
            "path": path,
            "offset": offset,
            "cant_bytes": cant_bytes,
            "operacion": 3,
        }

        # Con pickle encapsulamos o serializamos lo datos
        datos_serializados = pickle.dumps(datos)
        
        # hago la llamada con los datos serializados
        self._channel.sendall(datos_serializados)
        data = self._channel.recv(4096)
        data_deserialized = pickle.loads(data)

        # Desearializo los datos y retorno
        return data_deserialized.get("data_file")

    def closeFile(self, path):
        # armo el datos con path y el numero de operacion para el servidor
        datos = {"path": path, "operacion": 4}

        # Con pickle encapsulamos o serializamos lo datos
        datos_serializados = pickle.dumps(datos)
        
        # hago la llamada con los datos serializados
        self._channel.sendall(datos_serializados)
        data = self._channel.recv(4096)
        
        # Desearializo los datos y retorno
        data_deserializados = pickle.loads(data)
        return data_deserializados.get("close")

class Stub:

    def __init__(self, host='0.0.0.0', port="8090"):
        self._appliance = (host, int(port))
        self._channel = None
        self._stup = None

    def connect(self):
        try:
            self._channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._channel.connect(self._appliance)
            self._stub = FSStub(self._channel)
            return True if self._channel else False
        except Exception as e:
            print('Error when openning channel {}'.format(e))
            return False

    def disconnect(self):
        self._channel.close()
        self._channel = None

    def is_connected(self):
        return self._channel

    def list_files(self, path):
        if self.is_connected():
            return self._stub.ListFiles(path)
        return None
            
        # Agregados
    def open_file(self, path):
        return self._stub.openFile(path)

    def read_file(self, path, offset, cant_bytes):
        return self._stub.readFile(path, offset, cant_bytes)

    def close_file(self, path):
        return self._stub.closeFile(path)