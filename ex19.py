array = []

for i in range(5):
    n = int(input("Digite um número: "))
    array.append(n)

unique_numbers = []
for num in array:
    # se o numero NAO estiver na lista de numeros unicos, adiciona
    # se ele estiver, nao eh adicionado pq eh pra mostrar somente numeros unicos
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)

