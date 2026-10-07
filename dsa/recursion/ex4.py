def multip_rec(n1, n2):
    if n2 == 0:
        return 0
    if n2 < 0:
        return -multip_rec(n1, -n2)
    return n1 + multip_rec(n1, n2 - 1)

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print(multip_rec(n1, n2))
