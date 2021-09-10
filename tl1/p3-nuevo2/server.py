
class Server:

    def __init__(self, adapter):
        self.adapter = adapter

    def inicializar(self):
        print(" - ")
        print(" - -")
        print('Inicializando el servidor')
        print(" - -")
        print(" - ")        
        self.adapter.run()