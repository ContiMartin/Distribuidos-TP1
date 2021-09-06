
class Server:

    def __init__(self, adapter):
        self.adapter = adapter

    def inicializar(self):
        print("  ")
        print(" - - - - - - - -0- - - - - - - -")
        print('Inicializando el servidor')
        print("  ")
        print(" - - - - - - - -0- - - - - - - -")
        self.adapter.run()