true_password = 987654

while (True):
    password = int(input("Digite a sennha (6 dígitos): "))
    if password == true_password:
        print("Senha correta! Cofre aberto.")
        break
    else:
        print("Senha incorreta. Tente novamente.")