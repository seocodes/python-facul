class Fila():
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.final = -1 # ultimo que entrou
        self.inicio = 0 # proximo a sair
        self.elementos = 0
        self.valores = [None] * capacidade

    def fila_vazia(self):
        return self.elementos == 0

    def fila_cheia(self):
        return self.elementos == self.capacidade

    def ver_primeiro(self):
        if self.fila_vazia():
            return -1
        return self.valores[self.inicio]

    def enfileirar(self, valor): # movimenta a var final (ultimo inserido)
        if self.fila_cheia():
            print("FILA CHEIA")
            return 

        if self.final == self.capacidade - 1: # -1 pois self.final é por índice (comeca do 0)
            self.final = -1  # prepara o indice para voltar ao 0 (na prox iteração self.final += 1 vai deixar o final como 0 - inicio do vetor)

        self.final += 1
        self.valores[self.final] = valor
        self.elementos += 1

    def desenfileirar(self): # movimenta a var inicio (elemento a ser retirado)
        if self.fila_vazia():
            print("FILA VAZIA")
            return

        temp = self.valores[self.inicio]
        self.inicio += 1

        if self.inicio == self.capacidade:
            self.inicio = 0 # basicamente reinicia a fila

        self.elementos -= 1
        return temp  # elemento desenfileirado


fila = Fila(7)

# 1) Testa fila vazia
fila.desenfileirar()
# FILA VAZIA

# 2) Enfileira as letras do nome
for letra in "AUGUSTO":
    fila.enfileirar(letra)
    print(fila.valores)

# 3) Testa fila cheia
fila.enfileirar("X")
# É PRA MOSTRAR "FILA CHEIA"

# 4) Mostra o primeiro da fila
print("Primeiro:", fila.ver_primeiro())
# A

# 5) Desenfileira 3 vezes
print("Saiu:", fila.desenfileirar())  # A
print("Saiu:", fila.desenfileirar())  # U
print("Saiu:", fila.desenfileirar())  # G

# Verifica o novo primeiro
print("Novo primeiro:", fila.ver_primeiro())
# U

    
