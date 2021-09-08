import socket
import pickle
from p3b.structures import (
    Path, 
    PathFiles,
)

# Constante para el tamaño del buffer
#cant_buff = 1024

class FSStub:

    def __init__(self, canal):
        self._channel = canal

    def ListFiles(self, path):
        path = Path(path=path, operacion=1)
        self._channel.sendall(path)

        print("Llamo al open")
        peticion = {"path":path, "comando":1}
        peticion_serialized = pickle.dumps(peticion)
        self._channel.sendall(peticion_serialized)
        # funcion bloqueante, esperando que el servidor responda
        data = self._channel.recv(4096)
        data_Deserealized = pickle.loads(data)
        return data_Deserealized.get("paths")
        #path_files = PathFiles()
        #list_files = []
        #while self._channel.recv_into(path_files):
        #    list_files.append(path_files.values)

        #return list_files

    def Read(self,path,offset,cant_bytes):
        #self._channel.sendall(path)
        #request = self._channel.recv(cant_buff)
        #return request
        peticion = {
            "path": path,
            "offset": offset,
            "cant_bytes": cant_bytes,
            "comando": 3,
        }
        peticion_serialized = pickle.dumps(peticion)
        self._channel.sendall(peticion_serialized)
        data = self._channel.recv(4096)
        data_deserialized = pickle.loads(data)
        return data_deserialized.get("data_file")


    def openFile(self,path):
        print("Llamo al open")
        peticion = {"path":path, "comando":2}
        peticion_serialized = pickle.dumps(peticion)
        self._channel.sendall(peticion_serialized)
        # funcion bloqueante, esperando que el servidor responda
        data = self._channel.recv(4096)
        data_Deserealized = pickle.loads(data)

        return data_Deserealized.get("open")

class Stub:

    def __init__(self, host='0.0.0.0', port=8090):
        self._appliance = (host, port)
        self._channel = None
        self._stub = None

    def connect(self):
        """ Returns a gRPC open channel """
        print("entre al conect")
        try:
            self._channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._channel.connect(self._appliance)
            self._stub = FSStub(self._channel)
            
            print(self._stub)
            
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
            print("ACA ESTA EL LIO")
            return self._stub.ListFiles(path)
        print("ACA SALI DE ESTE LIO")
        return None

    def open_file(self, path):
        print("paso por el open file")
        self._stub.openFile(path)
        return None

    def read_file(self, path,offset, cant_bytes):
        if self.is_connected():
            return self._stub.Read(path,offset, cant_bytes)
        return None