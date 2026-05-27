votos = [0, 0, 0, 0, 0, 0]

while(True):
    print("""URNA ELEITORAL!
        1 - RENAN SANTOS
        2 - LULA
        3 - FLAVIO BOLSONARO
        4 - ZEMA (OU ZUMA, N LEMBRO O NOME DESSE CABA)
        5 - VOTO NULO
        6 - VOTO EM BRANCO
        0 - SAIR""")
    op = int(input("Digite uma opção: "))
    if(1 <= op <= 6):
        votos[op-1] += 1  # literalmente toda a logica dos ifs/elifs  abaixo
    # if(op==1):
    #     votos[0] += 1
    # elif(op==2):
    #     votos[1] += 1
    # elif(op==3):
    #     votos[2] += 1
    # elif(op==4):
    #     votos[3] += 1
    # elif(op==5):
    #     votos[4] += 1
    # elif(op==6):
    #     votos[5] += 1
    elif(op==0):
        break
    else:
        print("Opção inválida!")

print("Votos Renan Santos:", votos[0])
print("Votos Lula:", votos[1])
print("Votos Flávio Bolsonaro:", votos[2])
print("Votos Zema:", votos[3])
print("Votos Nulo:", votos[4])
print("Votos em Branco:", votos[5])