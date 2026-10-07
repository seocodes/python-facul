def decrescente(n):
    print(n)
    if n == 0:
        return
    decrescente(n - 1)

n = int(input("Digite um número: "))
decrescente(n)
