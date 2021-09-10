import socket
import pickle

cant_buff = 1024


class FSStub:

    def __init__(self, canal, file_system_adapter):
        self._channel = canal
        self._adapter = file_system_adapter
        self._process_request()

    def _process_request(self):
        #path = Path()
        #data = self._channel.recv_into(path)
        
        #data = self._channel.recv(cant_buff)

        #while True:
        #    if not data: 
        #        break

        #    if path.operacion == 1:
        #        path_ = path.path
        #        path_files = self._adapter.list_files(path_)

        #    for _path in path_files:
        #        self._channel.sendall(_path)

            data = self._channel.recv(cant_buff)
            if data:
                dataPickle = pickle.loads(data)
                if dataPickle is not None:
                    if dataPickle['operacion'] == 1:
                        path_files = self._adapter.list_files(dataPickle['value'])
                        request = { 'value': path_files}
                        requestPickle= pickle.dumps(request)
                        self._channel.send(requestPickle)

                    elif dataPickle['operacion'] == 2:
                        read_file = self._adapter.read_file(dataPickle)
                        request = { 'value': read_file}
                        requestPickle= pickle.dumps(request)
                        self._channel.sendall(requestPickle)
                    return 0
            else:
                return 1


class Stub:

    def __init__(self, adapter, port="8090"):
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
                from_client = ''
                self._stub = FSStub(connection, self._adapter)
                if self._stub._process_request():
                    print (client_address)
                    break
        except KeyboardInterrupt:
            connection.close()
            self.server.stop(0)
