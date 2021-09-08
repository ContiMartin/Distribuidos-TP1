import socket
#from p3b.structures import (Path)
import pickle

# Constante para el tamaño del buffer
# cant_buff = 1024

class FSStub:

    def __init__(self, canal, file_system_adapter):
        self._channel = canal
        self._adapter = file_system_adapter
        self._process_request()

    def _process_request(self):
        
        while True:    
            data = self._channel.recv(4096)
            
            if data:
                
                payload = pickle.loads(data)
                
                camino = payload.get("comando", -1)


                if camino is not None:
                    
                    #if dataPickle['comando'] == 1:
                    if camino == "1":

                        #path_files = self._adapter.list_files(dataPickle['value'])
                        
                        #path_files = self._adapter.list_files(path)

                        #request = { 'value': path_files}
                        #requestPickle = pickle.dumps(request)
                        #self._channel.send(requestPickle)

                        path = payload.get("path")
                        path_files = self._adapter.list_files(path)
                        response = {"paths": path_files}
                        response_serialized = pickle.dumps(response)
                        self._channel.sendall(response_serialized)

                    #elif dataPickle['comando'] == 2:
                    elif camino == "2":
                        #read_file = self._adapter.read_file(dataPickle["path"])
                        path = payload.get("path")
                        open = self._adapter.open_file(path)
                        response = {"open": open}
                        response_serialized = pickle.dumps(response)
                        self._channel.sendall(response_serialized)
                            
                    #elif dataPickle['comando'] == 3:
                    elif camino == "3":    
                        path = payload.get("path")
                        offset = payload.get("offset")
                        cant_bytes = payload.get("cant_bytes")
                        data_file = self._adapter.read_file(path, offset, cant_bytes)
                        response = {"data_file": data_file}
                        response_serialized = pickle.dumps(response)
                        self._channel.sendall(response_serialized)

                    #elif dataPickle['comando'] == 3:
                    elif camino == "4":
                        path = payload.get("path")
                        close = self._adapter.close_file(path)
                        response = {"close": close}
                        response_serialized = pickle.dumps(response)
                        self._channel.sendall(response_serialized)
                 
            else:
                return 1

class Stub:

    def __init__(self, adapter, port='8090'):
        self._port = int(port)
        self._adapter = adapter
        self.server = None
        self._stub = None

    def _setup(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('0.0.0.0', self._port))        

    def run(self):
        self._setup()
        self.server.listen()
        try:
            while True:
                connection, client_address = self.server.accept()
                self._stub = FSStub(connection, self._adapter)

        except KeyboardInterrupt:
            connection.close()
            self.server.stop(0)
