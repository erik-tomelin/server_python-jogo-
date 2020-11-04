#                     #
#   Cliente   #
#                    #

from socket import *

host = "localhost"
port = 8080
addr = (host, port)

c = socket(AF_INET, SOCK_STREAM)

c.connect(addr)

#-------------------------------#

while True:
    print("-------------------------------------------------------------")
    print("Bem Vindo")
    print("Você escolheu a opção 1 (Adivinhe o numero)")
    print(" ")
    print("Será gerado um numero aleatório entre 1 a 100")
    print("Seu dever é acerta-lo o mais rápido possivel")
    print(" ")
    valida = str(input("Precione 1 para jogar e qualquer tecla para sair: "))

    valida = valida.encode()
    valida = c.send(valida)
    sorteio = c.recv(1024)
    sorteio = sorteio.decode()
    sorteio = int(sorteio)

    print(" ")
    print("O valor foi gerado!")
    print(" ")
    while True:
        
        num = str(input("Escolha um numero de 1 a 100: "))

        num = num.encode()
        num = c.send(num)

        vitoria = c.recv(1024)
        vitoria = vitoria.decode()
        vitoria = int(vitoria)
        
        vez = c.recv(1024)
        vez = vez.decode()
        
        if (vitoria == 1):
            print(" ")
            print("Parabéns! Você acertou numero")
            print("O numero era", sorteio,
                      "e você acertou na tentativa", int(vez))
            #print("Sua pontuação foi", pontos)
            print("")
            
            valida_nw_game = input("Deseja jogar novamente? ( s / n ): ")
            valida_nw_game = valida_nw_game.encode()
            valida_nw_game = c.send(valida_nw_game)

        else:          
            resposta = c.recv(1024)  
            resposta = resposta.decode()
            print("")
            print(resposta)
            print("")
