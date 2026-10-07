n = int(input("Digite um número: "))

def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)
print(sum(n))
