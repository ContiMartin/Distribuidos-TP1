from client import Client
from p3a import ClientStub


# Para el p 3a
from p3a import ClientStub

# Para el p 3b
#from p3b import ClientStub

from datetime import datetime

# Obtiene la extencion del archivo, lo que este despues de un punto.
def Obtener_extension_de_archivo(path):
    extension = path.split(".").pop()
    return extension


def leer_archivo(cliente, path):

    can_open_file = cliente.abrir_archivo(path)

    if can_open_file:
        
        extension = Obtener_extension_de_archivo(path)
        
        today = datetime.now()
        
        # https://rico-schmidt.name/pymotw-3/datetime/index.html
        file_name = f"{today.strftime('%d-%m-%Y_%H:%M:%S')}.{extension}"
        
        # Open es una funcion de python para abrir archivos
        # necesita la ruta y los permisos
        # y lo que hacemos es que lo almacenamos en file
        file = open(file_name, "wb")
        
        print("Copiando el archivo...")
        file.close()
        cliente.cerrar_archivo(path)
        return True
    else:
        return False


def listar_archivos(path, cliente):
    archivos = cliente.listar_archivos(path)
    
    # Iterar por toda la lista y muestra archivo por archivo.
    for archivo in archivos:
        print(f"{archivo}")
    return True


def menu():
    print(". Donde buscar el archivo?:..")
    path = input()
    return path


def main():
    # Este Main no cambia por ahora
    stub = ClientStub("localhost", "50051")
    cliente = Client(stub)
    cliente.conectar()
    
    # Variable para poder salir del while
    salir = False

    while not salir:
        print(" - - - - - - - -0- - - - - - - -")
        print(" Menu - Sistemas Distribuidos 2021")
        print(" L - Leer y copiar Archivo")
        print(" V - Ver los archivos de un directorio")
        print(" S - Salir")
        print(" - - - - - - - -0- - - - - - - -")
        
        # Opcion ingresada por consola
        camino = input()

        try:
            
            # Segun la opcion entra en un camino o el otro
            camino = str(camino)
            if camino == "L":
                path = menu()
                print(f"Ruta ingresada: {path}")
                
                operation_result = leer_archivo(cliente, path)
                
                if operation_result:
                    print("Copia exitosa!")
                else:
                    print("Archivo no existe!")
            if camino == "V":
                path = menu()
                print(f"Ruta ingresada: {path}")
                operation_result = listar_archivos(path, cliente)
                
                if not operation_result:
                    print(f"Directorio vacio. {path}")
            elif camino == "S":
                
                # Desconecta y saluda el cliente.
                print("Saliendo")
                cliente.desconectar()
                print("Cliente Desconectado.")

                # Talvez esta de mas
                salir = True
                break
            else:
                print("Reimprimir MENU!")
        except ValueError:
            print("Opción Incorrectas")
        except KeyboardInterrupt:
            cliente.desconectar()
            salir = True
            break

if __name__ == '__main__':
    main()