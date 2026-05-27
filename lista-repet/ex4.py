# UM EMBAIXO DO OUTRO:
# i = 1
# while i<=20:
#     print(i)
#     i += 1

i = 1
while i<=20:
    # por padrao o end seria "\n", pulando uma linha
    print(i, end=" ")
    i += 1

# Forma muito compacta: 
# print(*range(1, 21))