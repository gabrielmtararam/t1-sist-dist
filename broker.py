import zmq
from constants import *


users_sockets = []
# next_user_socket = 5557
# Configuração de ZeroMQ
context = zmq.Context()
socket_pub = context.socket(zmq.PUB)
socket_receive = context.socket(zmq.SUB)
socket_receive.connect(f"{SUBSCRIBE_ADDR}{BROKER_PORT_RECEIVE}")
socket_pub.bind(f"{PUB_ADDR}{BROKER_PORT_PUB}")

print(f"received in {SUBSCRIBE_ADDR}{BROKER_PORT_RECEIVE}")

while True:
    combined_data = socket_receive.recv_pyobj()
    print(f"Mensagem recebida: {combined_data}")
    # aqui eu faria o gerenciamento de usuario e grupos, talvez criando um socket para cada grupo
