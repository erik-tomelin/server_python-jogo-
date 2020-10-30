import random
import time
import sys

while True:
    print("-------------------------------------------------------------")
    print("Bem Vindo")
    print("Você escolheu a opção 2 (Pedra, Papel, Tesoura)")
    print(" ")
    print("O seu oponente irá escolher uma das 3 opções")
    print("E você deve ganhar dele 5 vezes seguidas")
    print("Caso erre uma das 5 você volta para o inicio")
    print("Dependendo do tempo que você demorar pra responder, a sua pontuação diminuirá")
    print("Boa sorte :)")
    print(" ")
    valida = int(input("Precione 1 para jogar ou 2 voltar ao menu: "))

    if (valida == 1):
        seed = random.randint(1, 9)
        while True:
            if (seed == 1):
                escolja_pc = array(3,2,2,1,1)
            elif (seed == 2):
                
            elif (seed == 3):

            elif (seed == 4):

            elif (seed == 5):
                
            elif (seed == 6):
                
            elif (seed == 7):
                
            elif (seed == 8):
                
            elif (seed == 9):

            escolha = int(input("Escolha 1 entre as 3 opções 1[Pedra], 2[Papel] ou 3[Tesoura]: "))
            

    else:
        text = "Voltando ao menu..."
        for char in text:
            sys.stdout.write(char)
            time.sleep(0.1)
        break