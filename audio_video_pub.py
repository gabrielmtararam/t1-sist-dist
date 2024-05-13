import cv2
import zmq
import pyaudio
import numpy as np
import base64

# Configuração de ZeroMQ
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

# Configuração de captura de vídeo
cap = cv2.VideoCapture(0)

# Configuração de captura de áudio
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

while True:
    # Captura de vídeo
    ret, frame = cap.read()
    _, buffer = cv2.imencode('.jpg', frame)
    video_data = base64.b64encode(buffer).decode('utf-8')

    # Captura de áudio
    audio_data = stream.read(1024)
    audio_data = base64.b64encode(audio_data).decode('utf-8')

    # Envio de dados combinados
    combined_data = {"video": video_data, "audio": audio_data}
    socket.send_pyobj(combined_data)

cap.release()
stream.stop_stream()
stream.close()
audio.terminate()