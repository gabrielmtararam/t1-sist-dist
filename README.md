# t1-sist-dist
sudo apt-get install python3-pyaudio
criar venv ou usar o python do sistema
com a venv ativada ou não, dar cd ou utilizar o path do arquivo requirements e executa
pip install -r requirements.pip

para rodar o projeto, executar 

python audio_video_pub.py

python audio_video_subscriber.py 


Ideia  de implementação:

já temos como transmitir audio e video e texto, do servidor para um cliente, e do cliente para o servidor

Falta:
- Implementar um usuario (vai precisar ter uma identificação qualquer pra diferenciar ele dos outros subscribers)
   - Usuario manda uma requisição, ex: subscribe gabrielmt canal1, nesse momento servidor registra e cria um canal para o usuario com o grupo.
   - Servidor tem uma lista de usuarios cadastrados nesse grupo/canal, e o socket de cada um deles.
   - Usuario que quer enviar alguma transmissão para o servidor vai enviar
    {"usuario":"identificacao_do_usuario", grupo":"identificacao_do_grupo", audio": audio_data_se_tiver, "video":video_data_se_tiver, "text":text_data_se_tiver}
    -Servidor sempre que chegar uma mensagem, vai identificar o grupo, e reenviar para todos os usuarios cadastrados no grupo.
    - Servidor quando enviar para o usuario, vai serguir o mesmo padrão, falar qual usuario enviou, o grupo, e os dados.