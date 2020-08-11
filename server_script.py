import socket

socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 80
socket_object.bind((host, port))
socket_object.listen(5)                 # The number of devices allowed to connect
helpful_message = 'You are connected. Type "/h" to print helpful information or type "exit()" to disconnect.'

while True:
    client_socket, address = socket_object.accept()

    print(f'Connection established from {address}.')         # Has no username or IP address as arguments
    client_socket.send(helpful_message.encode('ascii'))
    client_socket.close()
