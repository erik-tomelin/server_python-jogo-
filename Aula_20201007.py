        horas = input("Qtd de horas mensais: ")
        horas = float(horas)
        valor = float(valor)
        horas = float(horas)

        salBruto = horas * valor
        valINSS = salBruto * 0.08
        if salBruto <= 1500 :
            valIRRF = 0
        elif 1500 < salBruto <= 3000 :
            valIRRF = salBruto * 0.07
        elif 3001 < salBruto <= 8000 :
            valIRRF = salBruto * 0.1
        elif 8001 < salBruto <= 12000 :
            valIRRF = salBruto * 0.15
        else:
            valIRRF = salBruto * 0.2
        salLiq = salBruto - valINSS - valIRRF

        registro = [nome, valHora, horas, salBruto, valINSS, valIRRF, salLiq]
        folhaPgto.append(registro)
    
    '''
    if op == "2":
        print("")
        print("")
        print("")
        print("-----------------------------")
        print("Consulta - Folha de pagamento")
        print("-----------------------------")
        print("Existem ", len(folhaPgto), " registro na tabela")
        reg = input("Qual registro deseja consultar : ")
        reg = int(reg)

        if reg < 1 or reg > len(folhaPgto) :
            print("Numero de registro invalido")
        else:
            reg = reg - 1
            print("Nome                : ", folhaPgto[reg] [0])
            print("Valor da hora       : ", folhaPgto[reg] [1])
            print("Qtd de horas        : ", folhaPgto[reg] [2])
            print("Salario Bruto       : ", folhaPgto[reg] [3])
            print("Desconto de INSS    : ", folhaPgto[reg] [4])
            print("Desconto de IRRF    : ", folhaPgto[reg] [5])
            print("Salario Liquido     : ", folhaPgto[reg] [6])
    '''