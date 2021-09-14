import socket
import pickle


# Libreria para hilos
import threading

cant_buff = 1024

class FSStub(threading.Thread):
    def __init__(self, canal, file_system_adapter):
        
        # Defino para hilos
        threading.Thread.__init__(self)
        
        self._channel = canal
        self._adapter = file_system_adapter
        
    def run(self):
        while True:







            data = self._channel.recv(4096)
            

            datos = pickle.loads(data)
            comando = datos.get("operacion", -1)
            if comando == 1:
                # Listar archivo
                # armo el path con los datos
                path = datos.get("path")
                path_files = self._adapter.list_files(path)
                
                # armo la respuesta con los datos
                respuesta = {"paths": path_files}
                
                # con pickle armo la respuesta serializada
                respuesta_serializada = pickle.dumps(respuesta)
                self._channel.sendall(respuesta_serializada)
            
            elif comando == 2:
                # Abrir archivo
                path = datos.get("path")
                open = self._adapter.open_file(path)
                
                # armo la respuesta
                respuesta = {"open": open}
                
                # con pickle armo la respuesta serializada
                respuesta_serializada = pickle.dumps(respuesta)
                self._channel.sendall(respuesta_serializada)
            
            elif comando == 3:
                # Leer archivo
                # armo el path con los datos
                path = datos.get("path")
                offset = datos.get("offset")
                cant_bytes = datos.get("cant_bytes")
                
                # armo el archivo con los datos
                datos_archivo = self._adapter.read_file(path, offset, cant_bytes)
                
                # armo la respuesta, ya con el close
                respuesta = {"data_file": datos_archivo}
            
                # con pickle armo la respuesta serializada
                respuesta_serializada = pickle.dumps(respuesta)
                self._channel.sendall(respuesta_serializada)
            
            elif comando == 4:
                # Cerrar archivo
                # armo el path con los datos
                path = datos.get("path")
                # defino el close
                close = self._adapter.close_file(path)
                # armo la respuesta, ya con el close
                respuesta = {"close": close}
                # con pickle armo la respuesta serializada
                respuesta_serializada = pickle.dumps(respuesta)
                self._channel.sendall(respuesta_serializada)

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
                # Variable para poder salir del while
                print(" ")
                print(" - - - - - - - -0- - - - - - - -")
                print(" Menu del servidor - Sistemas Distribuidos 2021")
                print(" Ingrese cantidad de hilos a crear")
                print(" ")
                
                # Opcion ingresada por consola
                nuemro = input()
                            
                
                try:
            
                    # Segun la opcion entra en un camino o el otro
                    camino = int(camino)
                    if camino == "":
                    print(" ")
                    print(f"Ruta ingresada: {path}")
                
                
                
                elif camino == "0": 
                    # Desconecta y saluda el cliente.
                    print(" ")
                    print("Saliendo")
                    
                    
                    break
                
                
                
                
                
                connection, client_address = self.server.accept()
                print(" ")
                print(" Cliente: ", str(client_address))
                
                # Como era antes
                # self._stub = FSStub(connection, self._adapter)
                # Como queda con hilos
                thread = FSStub(connection, self._adapter)
                print(" Atendido por el Hilo:", thread.getName())
                
                thread.start()

        except KeyboardInterrupt:
            connection.close()
            self.server.stop(0)