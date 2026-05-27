# ah sla botei esse try pq sim
try:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
except ValueError:
    print("Digite um número válido.")
    exit()

sum = 0
for i in range(n1, n2 + 1):
    sum += i
    print(i, end=" ")
print()
print(f"A soma dos números entre {n1} e {n2} é {sum}.")