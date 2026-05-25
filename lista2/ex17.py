number = int(input("Type a number between 100 and 999: "))

if 100 <= number <= 999:
    print("Centena: ", number // 100) # // = divisão inteira, remove a parte decimal, se tiver
    print("Dezena: ", (number % 100) // 10) # % = módulo, retorna o resto da divisão
    print("Unidade: ", number % 10)
else:
    print("Invalid number")
