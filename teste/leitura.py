while True:
    texto = input("Digite seu nome em 3 letras: ")
    cont_texto = len(texto)

    if ( cont_texto > 3):
        
        print("\n", "informe um numero de apenas 3 letras ", "\n")
    else:
        break
    
pontos = 500

arquivo = open('dados.txt','a') 
arquivo.write(texto  +  " - ", pontos+ "\n")
arquivo = open('dados.txt', 'r')

Lnome1 = arquivo.readline()
Lponto1 = arquivo.readline()
Lnome2 = arquivo.readline()
Lponto2 = arquivo.readline()
Lnome3 = arquivo.readline()
Lponto3 = arquivo.readline()
Lnome4 = arquivo.readline()
Lponto4 = arquivo.readline()
Lnome5 = arquivo.readline()
Lponto5 = arquivo.readline()
Lnome6 = arquivo.readline()
Lponto6 = arquivo.readline()
Lnome7 = arquivo.readline()
Lponto7 = arquivo.readline()
Lnome8 = arquivo.readline()
Lponto8 = arquivo.readline()
Lnome9 = arquivo.readline()
Lponto9 = arquivo.readline()

arquivo.close()
