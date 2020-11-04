nome    = "Erik"
valHora = float(input("Digite o seu salário hora: "))
qtdSem1 = float(input("Digite o valor da semana1: "))
qtdSem2 = float(input("Digite o valor da semana2: "))
qtdSem3 = float(input("Digite o valor da semana3: "))
qtdSem4 = float(input("Digite o valor da semana4: "))

salBruto = (qtdSem1 + qtdSem2 + qtdSem3 + qtdSem4) 
valINSS = salBruto * 0.08

if salBruto <= 1500 :
    valIRRF = 0
elif salBruto > 1500 and salBruto <= 3000 :
    valIRRF = salBruto * 0.07
elif salBruto > 3000 and salBruto <= 8000 :
    valIRRF = salBruto * 0.10
elif salBruto > 8000 and salBruto <= 12000 :
    valIRRF = salBruto * 0.15
else:
    valIRRF = salBruto * 0.20

salLiqui = salBruto - valINSS - valIRRF

print("O salário líquido do ", nome , " é de R$ ", salLiqui)

