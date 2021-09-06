from file_system import FS
from server import Server
from p3b import ServerStub

def main():
    stub = ServerStub(FS(), '50051')
    servidor = Server(stub)
    servidor.inicializar()

if __name__ == '__main__':
    main()