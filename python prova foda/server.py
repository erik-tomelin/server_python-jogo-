#                       #
#   Servidor   #
#                       #

from socket import *
import random

host = "localhost"
port = 8080
addr = (host, port)

s = socket( AF_INET, SOCK_STREAM )

s.bind( addr )
s.listen(1)

print ("aguardando conexão")

con, ender = s.accept()
print (" ")
print ("conectado")
        
vez = 0

while True:

    valida = con.recv(1024)
    valida = valida.decode()

    if (valida == '2'):
        print("Encerrando...")
        s.close()
    
    vez = vez + 1

    print("vez - ",vez)
    
    if (vez == 1 ):
        sorteio = str(random.randint(1, 100))
        print(sorteio)
        sorteio = sorteio.encode()
        con.send(sorteio)
        
    num = con.recv(1024)
    num = num.decode()

    print("O numero escolhido pelo clinte foi:", num)

    if (int(num) == int(sorteio)):
        vitoria = 1
        
        vitoria = str(vitoria)
        vitoria = vitoria.encode()
        con.send(vitoria)

        vez = str(vez)
        vez = vez.encode()
        con.send(vez)
        vez = int(vez)

        valida_nw_game = con.recv(1024)
        valida_nw_game = valida_nw_game.decode()

        if (valida_nw_game == 's'):
            vez = 0
        elif (valida_nw_game == 'n'):
            print("Encerrando...")
            s.close()
        
    else:
        vitoria = 0

        vitoria = str(vitoria)
        vitoria = vitoria.encode()
        con.send(vitoria)

        vez = str(vez)
        vez = vez.encode()
        con.send(vez)
        vez = vez.decode()
        vez = int(vez)

        if (vez == 1):
            sorteio = sorteio.decode()
        
        if (num > sorteio):
            resposta = "O valor sorteado é menor"
        elif (num < sorteio):
            resposta = "O valor sorteado é maior"
            
        resposta = resposta.encode()
        con.send(resposta)
        continue
