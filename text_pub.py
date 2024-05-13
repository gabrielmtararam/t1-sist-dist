import zmq

# Configuração de ZeroMQ
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5557")

print("Publicador de texto iniciado. Digite suas mensagens abaixo:")

while True:
    message = input("Mensagem: ")
    socket.send_string(message)