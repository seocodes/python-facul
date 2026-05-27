maior = None

for i in range(0, 5):
    num = int(input("Digite um número: "))
    if maior is None or num > maior:
        maior = num

print(f"O maior número é: {maior}")
