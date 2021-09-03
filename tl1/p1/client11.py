from stub import Stub
from mock_stub import MockStub
from client import Cliente

def main():
    # definicion de los stubs stub y mock_stub
    stub = Stub('localhost', 8090)
    mock_stub = MockStub('localhost', 8090)

    cliente = Cliente(stub)

    cliente.conectar()

    while True:
        print("Ingrese un mensaje para mandar al Servidor")
        user_mensaje = input()

        cliente.enviar(user_mensaje)

        mensaje = cliente.recibir()
        print(f"Respuesta: {mensaje}")

        if user_mensaje == "x":
            break

    cliente.desconectar()

main()
