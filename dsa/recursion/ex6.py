def pares(n):
    if n == 0:
        print(0)
        return
    pares(n - 2)
    print(n)

n = int(input("Digite um número par: "))
pares(n)
