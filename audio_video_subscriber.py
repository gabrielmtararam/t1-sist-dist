import cv2
import zmq
import pyaudio
import numpy as np
import base64

# Configuração de ZeroMQ
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, '')

# Configuração de reprodução de áudio
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True, frames_per_buffer=1024)

while True:
    # Recebimento de dados combinados
    combined_data = socket.recv_pyobj()
    video_data = base64.b64decode(combined_data['video'])
    audio_data = base64.b64decode(combined_data['audio'])

    # Decodificação e exibição do vídeo
    jpg_as_np = np.frombuffer(video_data, dtype=np.uint8)
    frame = cv2.imdecode(jpg_as_np, flags=1)
    cv2.imshow("Video", frame)

    # Reprodução de áudio
    stream.write(audio_data)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
stream.stop_stream()
stream.close()
audio.terminate()