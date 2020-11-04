#Servidor

from socket import *

servidor = socket(AF_INET, SOCK_STREAM)
tuplaEscuta = ('',12000)
servidor.bind( tuplaEscuta )
servidor.listen(True)

# [matricula, nome, valorHora, horas]

dadosFolha = []
dadosFolha.append([1, "Cebolinha", 12.00, 40])
dadosFolha.append([2, "Cascão"   , 11.30, 40])
dadosFolha.append([3, "Xaveco"   , 8.90 , 30])

while True:
    conexao, endereco = servidor.accept()

    mensagem = conexao.recv(1024)
    mensagem = mensagem.decode()

    comando = mensagem[0]

    if comando == "M":
        msgEmPartes = mensagem.split("-")
        matricula   = int(msgEmPartes[1])
        
        resposta = "NE"
        for registro in dadosFolha:
            if registro[0] == matricula :
                resposta = "R-" + str(registro[0]) + "-" + registro[1] + "-" + str(registro[2]) + "-" + str(registro[3])
        
    elif comando == "C":
        # cadastra um funcionário
        resp = "NI"
    else:
        # comando não reconhecido
        resposta = "NR"

    print("Recebido: ", mensagem)
    print("Respondido: ", resposta)
    print(" ")
    resposta = resposta.encode()
    conexao.send(resposta)
    conexao.close()
