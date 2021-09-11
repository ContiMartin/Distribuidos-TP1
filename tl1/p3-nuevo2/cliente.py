from client import Client
from p3b import ClientStub

#from datetime import datetime

CANT_BYTES = 100

# Obtiene la extencion del archivo, lo que este despues de un punto.
def Obtener_extension_de_archivo(path):
    extension = path.split(".").pop()
    return extension


def leer_archivo(cliente, path):

    can_open_file = cliente.abrir_archivo(path)

    if can_open_file:
        
        extension = Obtener_extension_de_archivo(path)
        
        #today = datetime.now()
        offset = 0

        print(". Ingrese nombre de archivo copiado nuevo..")
        path_de_archivo = input()

        # https://rico-schmidt.name/pymotw-3/datetime/index.html
        file_name = f"{path_de_archivo}.{extension}"
        
        # Open es una funcion de python para abrir archivos
        # necesita la ruta y los permisos
        # y lo que hacemos es que lo almacenamos en file
        file = open(file_name, "wb")
        
        print("Copiando el archivo...")
        
        
        while True:
            bytes_leidos = cliente.leer_archivo(
                path,
                offset,
                CANT_BYTES,
            )
            offset += CANT_BYTES
            
            print("antes de escribir")

            file.write(bytes_leidos)

            print("despues de escribir")


            if len(bytes_leidos) == 0:
                break
        
        
        
        
        file.close()
        cliente.cerrar_archivo(path)
        return True
    else:
        return False


def listar_archivos(path, cliente):
    archivos = cliente.listar_archivos(path)
    if len(archivos) == 0:
        return False
    #print(f"Se encontraron {len(archivos)} archivos:")
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
                    print("Descarga exitosa!")
                else:
                    print("No se encontró el archivo, vuelva a intentar")

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