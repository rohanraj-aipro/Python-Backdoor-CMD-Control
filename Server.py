import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 8081

server = socket.socket()
server.bind((HOST, PORT))

print('server Started')
print('Listening for Client Connection')
server.listen(1)
client, client_addr = server.accept()

print(f'{client_addr} Client connected to the server !!')

while True:
    command = input('Enter Command')
    command = command.encode()
    client.send(command)
    print('command sent!')
    output = client.recv(1024)
    output = output.decode()
    print(f'Output:{output}')

