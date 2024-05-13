import zmq

# Configuração de ZeroMQ
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5557")
socket.setsockopt_string(zmq.SUBSCRIBE, '')

print("Assinante de texto iniciado. Aguardando mensagens...")

while True:
    message = socket.recv_string()
    print(f"Mensagem recebida: {message}")