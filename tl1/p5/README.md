### Pasos para generar las clases necesarias de gRPC.

0. Contar con grpcio y grpcio-tools
        pip install grpcio
        pip install grpcio-tools

1. Definir las funciones

2. Defininir la especificación

3. Ejecutar

    ```sh
    python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. file_system.proto
    ```
    
    > Notese que al final del comando figura el archivo de protocol buffer (file_system.proto) para la generación de las clases necesarias.

4. Crear el servidor

5. Crear un cliente


### Bibligrafia
- https://grpc.io/docs/languages/python/basics/
- https://developers.google.com/protocol-buffers/docs/proto3#any
