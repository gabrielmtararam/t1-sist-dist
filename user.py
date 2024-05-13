import zmq
from constants import *

# Configuração de ZeroMQ
context = zmq.Context()
socket_pub = context.socket(zmq.PUB)
socket_receive = context.socket(zmq.SUB)

# invertido pois o canal que envia eh o que o outro recebe
socket_receive.connect(f"{SUBSCRIBE_ADDR}{BROKER_PORT_PUB}")
socket_pub.bind(f"{PUB_ADDR}{BROKER_PORT_RECEIVE}")

print(f"publish in {PUB_ADDR}{BROKER_PORT_RECEIVE}")


while True:
    message_type = input("digite o tipo da mensagem\n"
                         "1- Digitar nome do usuario\n"
                         "2- Se increver em grupo:\n ")
    message_value = input("digite o nome do usuário ou grupo")
    message_type = int(message_type)

    message_content = None

    if message_type == 1:
        message_content = {
            "message_type": SET_USER_TYPE,
            "content": message_value,
        }
    elif message_type == 2:
        message_content = {
            "message_type": SUBSCRIBE_GROUP,
            "content": message_value,
        }

    print(f"message_content {message_content}")
    if message_content:
        print(f"VAI ENVIAR")
        socket_pub.send_pyobj(message_content)