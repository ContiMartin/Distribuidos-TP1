import socket
from structures import Path

class FSStub:

    def __init__(self, canal, file_system_adapter):
        self._channel = canal
        self._adapter = file_system_adapter
        self._process_request()

    def _process_request(self):
        path = Path()
        data = self._channel.recv_into(path)
        if not data: break

        if path.operacion == 1:
            path_ = path.path
            path_files = self._adapter.list_files(path_)

            for _path in path_files:
                self._channel.sendall(_path)

class Stub:

    def __init__(self, adapter, port='8090'):
        self._port = port
        self._adapter = adapter
        self.server = None
        self._stub = None

    def _setup(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('0.0.0.0', self.port))        

    def run(self):
        self._setup()
        self.server.listen()
        try:
            while True:
                connection, client_address = server.accept()
                from_client = ''
                self._stub = FSStub(connection, self._adapter)

        except KeyboardInterrupt:
            connection.close()
            self.server.stop(0)
