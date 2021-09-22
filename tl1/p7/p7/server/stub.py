from concurrent.futures.thread import ThreadPoolExecutor
import socket
import pickle



cant_buff = 1024

def FSStub(canal, file_system_adapter):
        while True:
            
            data = canal.recv(4096)
            

            datos = pickle.loads(data)
            comando = datos.get("operacion", -1)
            if comando == 1:
                # Listar archivo
                # armo el path con los datos
                path = datos.get("path")
                path_files = file_system_adapter.list_files(path)
                
                # armo la respuesta con los datos
                respuesta = {"paths": path_files}
                
                # con pickle armo la respuesta serializada
                respuesta_serializada = pickle.dumps(respuesta)
                canal.sendall(respuesta_serializada)
            
            elif comando == 2:
                # Abrir archivo
                path = datos.get("path")
                open = file_system_adapter.open_file(path)
                
                # armo la respuesta
                respuesta = {"open": open}
                
                # con pickle armo la respuesta serializada
                respuesta_serializada = pickle.dumps(respuesta)
                canal.sendall(respuesta_serializada)
            
            elif comando == 3:
                # Leer archivo
                # armo el path con los datos
                path = datos.get("path")
                offset = datos.get("offset")
                cant_bytes = datos.get("cant_bytes")
                
                # armo el archivo con los datos
                datos_archivo = file_system_adapter.read_file(path, offset, cant_bytes)
                
                # armo la respuesta, ya con el close
                respuesta = {"data_file": datos_archivo}
            
                # con pickle armo la respuesta serializada
                respuesta_serializada = pickle.dumps(respuesta)
                canal.sendall(respuesta_serializada)
            
            elif comando == 4:
                # Cerrar archivo
                # armo el path con los datos
                path = datos.get("path")
                # defino el close
                close = file_system_adapter.close_file(path)
                # armo la respuesta, ya con el close
                respuesta = {"close": close}
                # con pickle armo la respuesta serializada
                respuesta_serializada = pickle.dumps(respuesta)
                canal.sendall(respuesta_serializada)

class Stub:
    def __init__(self, adapter, port="8090"):
        self._port = int(port)
        self._adapter = adapter
        self.server = None
        self._stub = None
        self._executor = None

    def _setup(self, hilos):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('0.0.0.0', self._port)) 
        self._executor = ThreadPoolExecutor(int(hilos))      

    def run(self):
        print(" ")
        print(" - - - - - - - -0- - - - - - - -")
        print(" Menu del servidor - Sistemas Distribuidos 2021")
        print(" Ingrese cantidad de hilos a crear")
        print(" ")
        hilos = input()
        self._setup(hilos)
        self.server.listen()
        try:
            while True:
                connection, client_address = self.server.accept()
                print("hilos:", hilos)
                print(f"Conectando al {client_address[0]}:{str(client_address[1])}\n")                
                self._executor.submit(FSStub, connection, self._adapter)

        except KeyboardInterrupt:
            self.server.stop(0)
            