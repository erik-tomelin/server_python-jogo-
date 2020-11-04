horas = input("Qtd de horas mensais  : ")
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
