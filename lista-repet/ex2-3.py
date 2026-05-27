sum = 0
positive = 0
negative = 0

for i in range(4):
    num = int(input("Digite um número: "))
    sum += num
    if num > 0:
        positive += 1
    else:
        negative += 1

avg = sum / 4
print(f"Média: {avg:.2f}")
print("Números positivos:", positive)
print("Números negativos:", negative)
total = positive + negative
print("Perecentual positivo X negativo:", (positive / total)*100, "X", (negative / total)*100)