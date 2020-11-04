while True :
    print("            ")
    print("----Menu----")  
    print("            ")
    print("1 - Cadastro")
    print("2 - Consulta")
    print("3 - Listagem")
    print("0 - Sair")
    opcao = input("Opcao : ")

    if opcao == "0" :
        break
    elif opcao == "1":
        while True :
            print("")
            print ("---Cadastro---")
            print("")
            login  = input("    Login     : ")
            senha1 = input("    Senha     : ")
            senha2 = input("Repetir senha : ")

            if senha1 == senha2 :
                print("")
                print ("Cadastro altenticado")
                print ("Seja bem-vindo ", login, " estavamos esperando por você")
                print("")
                break
            else:
                print ("Cadastro falho")
    elif opcao == "2" :
        print("")
        print ("Dois")
    elif opcao == "3" :
        print("")
        print("Tres")
    else:
        print("")
        print("CU")
    