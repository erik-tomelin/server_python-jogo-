import random
import time
import sys

pontos = 10000
vez = 0
pontua = 800

while True:
    print("-------------------------------------------------------------")
    print("Bem Vindo")
    print("Você escolheu a opção 1 (Adivinhe o numero)")
    print(" ")
    print("Será gerado um numero aleatório entre 1 a 100")
    print("Seu dever é acerta-lo o mais rápido possivel")
    print("Quanto mais rapido acertar, mais pontos ganhará.")
    print("Chegando a uma pontuação máxima de 10000 pontos")
    print("Caso sua pontuação chege a 0, você perde")
    print(" ")
    valida = int(input("Precione 1 para jogar ou 2 voltar ao menu: "))
    
    if (valida == 1):
        sorteio = random.randint(1, 100)
        while True:

            vez = vez + 25

            if (vez == 0):
                num = int(input("O valor foi gerado, escolha um numero de 1 a 100: "))
                print(" ")
            else:
                num = int(input("Escolha um numero de 1 a 100: "))
                print(" ")
            
            if (num == sorteio):
                print(" ")
                print("Parabéns! Você acertou numero")
                print("O numero era", sorteio, "e você acertou na tentativa", int(vez/25))
                print("Sua pontuação foi", pontos)
                gravar = input("Deseja gravar a sua pontuação? ( s / n )")
                if (gravar == 'n'):
                    break
                elif (gravar == 's'):
                    while True:
                        bd_j = input("Escolha um nome de até 3 letras para registrar: ")
                        if (len(bd_j) == 0 or len(bd_j) > 3):
                            print("Favor escolher apenas 3 caracteres")
                            continue
                        else:
                            print(bd_j,"-",pontos)
                            break

                    valida = input("Deseja jogar novamente? ( s / n )")
                    if (valida == 'n'):
                        break
                    elif (valida == 's'):
                        sorteio = random.randint(1, 100)
                        pontos = 5000
                        vez = 0
            else:
                pontua = pontua - vez
                pontos = pontos - pontua

                if (pontos <= 0):
                    print ("Você perdeu :c")
                    print ("Seus pontos chegaram a 0")
                    print ("O numero sorteado era",sorteio)
                    
                    valida = input("Deseja jogar novamente? ( s / n )")
                    if (valida == 'n'):
                        break
                    elif (valida == 's'):
                        sorteio = random.randint(1, 100)
                        pontos = 5000
                        vez = 0
                else:
                    print(pontos)
                    if (num > sorteio):
                        print("O valor sorteado é menor")
                    elif (num < sorteio):
                        print("O valor sorteado é maior")
        break
    else:
        text = "Voltando ao menu..."
        for char in text:
            sys.stdout.write(char)
            time.sleep(0.1)
        break
