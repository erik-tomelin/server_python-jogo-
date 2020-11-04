#
# Programa no Cliente
#

from socket import *

# AF_INET -> IPV4
# SOCK_STREAM -> TCP

client = socket( AF_INET, SOCK_STREAM )
tuplaDestino = ('localhost', 12000)
client.connect ( tuplaDestino )

mensagem = input("Enviar mensagem: ")
mensagem = mensagem.encode() # Encode -> Tranforma Str em byte

client.send(mensagem)

resposta = client.recv(1024)
resposta = resposta.decode() # Decode -> Volta de Byte pra Str

print("O sever respondeu : ",resposta)

client.close()
