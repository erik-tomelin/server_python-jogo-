#
# Programa no servidor
#

from socket import *

server = socket( AF_INET, SOCK_STREAM )
tuplaEscuta = ( '', 12000 )
server.bind( tuplaEscuta )

server.listen(True)

while True:
    conexao, endereco = server.accept()

    mensagemRecebida = conexao.recv(1024)
    mensagemRecebida = mensagemRecebida.decode()

    print("Recebi a mensagem : ", mensagemRecebida)

    if mensagemRecebida == "oi":
        resposta = "Olá, em que posso ajudar?"
    else:
        resposta = "não entendi"

    resposta = resposta.encode()
    conexao.send(resposta)
    conexao.close()
