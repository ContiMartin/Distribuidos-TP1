import socket


server_address = (('0.0.0.0', 8090))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_address)
server.listen()

message = 'I am Power SERVER\n'

while True:
	print('Servidor FULL disponible!')
	connection, client_address = server.accept()
	from_client = ''

	while True:
		data = connection.recv(4096)
		if data.decode() == 'x':break
		# Aqui acumula mensajes, y sale si llega una x
		from_client += data.decode()
		connection.send(message.encode('utf-8'))

	print(from_client)
	print('El Cliente pidio Salir!.')
	connection.send(data)
	connection.close()
	print('Cliente Desconectado \n')