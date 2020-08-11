import socket

username = input('Enter your name/username: ')
socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 80

socket_object.connect((host, port))
received_message = socket_object.recv(1024)
socket_object.close()

print(received_message.decode('ascii'))
