num = []

for i in range(6):
    n = int(input("Digite um número: "))
    num.append(n)

even = []
odd = []
for n in num:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)

print("Números pares:", even)
print("Soma dos números pares:", sum(even))
print("Números ímpares:", odd)
print("Quantidade de números ímpares:", len(odd))
