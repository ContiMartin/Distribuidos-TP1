import socket

from p3b.structures import (
    Path, 
    PathFiles,
)

# Constante para el tamaño del buffer
cant_buff = 1024

class FSStub:

    def __init__(self, canal):
        self._channel = canal

    def ListFiles(self, path):
        path = Path(path=path, operacion=1)
        self._channel.sendall(path)

        path_files = PathFiles()
        list_files = []
        while self._channel.recv_into(path_files):
            list_files.append(path_files.values)

        return list_files

    def Read(self,path):
        self._channel.sendall(path)
        request = self._channel.recv(cant_buff)
        return request

class Stub:

    def __init__(self, host='0.0.0.0', port='8090'):
        self._appliance = (host, port)
        self._channel = None
        self._stup = None

    def connect(self):
        """ Returns a gRPC open channel """
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


    def read_file(self, path):
        if self.is_connected():
            return self._stub.Read(path)
        return None