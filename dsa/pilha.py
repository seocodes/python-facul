import numpy as np

class Pilha():
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = []

    def pilha_vazia(self):
        return len(self.valores) == 0

    def pilha_cheia(self):
        return len(self.valores) == self.capacidade

    def ver_topo(self):
        if self.pilha_vazia():
            return -1
        
        return self.valores[self.topo]

    def empilhar(self, valor):
        if self.pilha_cheia():
            print("PILHA CHEIA")
            return

        self.valores.append(valor)
        self.topo += 1

    def desempilhar(self):
        if self.pilha_vazia():
            print("PILHA VAZIA")
            return

        valor = self.valores.pop()
        self.topo -= 1
        return valor

# Criando uma pilha com capacidade 6
pilha = Pilha(7)

# a) Testar pilhaVazia() através de desempilhar()

print("A) Testando pilha vazia:")
pilha.desempilhar()

# b) Empilhar cada caractere do primeiro nome

print("\nB) Empilhando o nome:")

nome = "AUGUSTO"

for letra in nome:  # vai iterando pelos caracteres e insere
    pilha.empilhar(letra)
    print(f"Empilhando: {letra}")

# c) Testar pilhaCheia() através de empilhar()

print("\nC) Testando pilha cheia:")
pilha.empilhar("X")

# d) Verificar o elemento no topo


print("\nD) Elemento no topo:")
print("Topo:", pilha.ver_topo())

# e) Desempilhar três vezes e verificar o topo

print("\nE) Desempilhando três vezes:")

for i in range(3):
    elemento = pilha.desempilhar()
    print(f"Desempilhado: {elemento}")

print("Novo topo:", pilha.ver_topo())
        

    
