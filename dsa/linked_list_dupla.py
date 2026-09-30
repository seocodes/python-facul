class No:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None

    def mostrar_no(self):
        print(self.valor, end=" ")


class ListaDupla:
    def __init__(self):
        self.primeiro = None

    def inserir_inicio(self, valor):
        novo = No(valor)

        # O novo nó entra antes de quem era o primeiro.
        novo.proximo = self.primeiro

        # Se já existia um primeiro nó, ele precisa apontar
        # de volta para o novo nó.
        if self.primeiro is not None:
            self.primeiro.anterior = novo

        self.primeiro = novo

    def mostrar(self):
        if self.primeiro is None:
            print("Lista vazia")
            return

        atual = self.primeiro

        # Percorre a lista até não existir mais um próximo nó.
        while atual is not None:
            atual.mostrar_no()
            atual = atual.proximo

        print()

    def excluir_inicio(self):
        if self.primeiro is None:
            return None

        removido = self.primeiro
        self.primeiro = self.primeiro.proximo

        # O novo primeiro não pode continuar apontando
        # para o nó que acabou de ser removido.
        if self.primeiro is not None:
            self.primeiro.anterior = None

        removido.proximo = None
        return removido

    def pesquisar(self, valor):
        atual = self.primeiro

        while atual is not None:
            if atual.valor == valor:
                return atual

            atual = atual.proximo

        return None

    def excluir_qualquer(self, valor):
        atual = self.pesquisar(valor)

        if atual is None:
            return None

        # Se for o primeiro, já existe uma função própria para isso.
        if atual == self.primeiro:
            return self.excluir_inicio()

        # O nó anterior pula o nó que será removido.
        atual.anterior.proximo = atual.proximo

        # Se houver um nó depois, ele também precisa ser religado.
        if atual.proximo is not None:
            atual.proximo.anterior = atual.anterior

        atual.anterior = None
        atual.proximo = None

        return atual


lista = ListaDupla()
nome = "Augusto"

# a) Inserção dos caracteres do primeiro nome
for caractere in nome:
    lista.inserir_inicio(caractere)

# b) Impressão dos elementos
print("Lista após as inserções:")
lista.mostrar()

# c) Exclusão do primeiro elemento
removido = lista.excluir_inicio()
print("Primeiro elemento excluído:",
      removido.valor if removido else None)

# d) Verificação da exclusão
print("Lista após excluir o primeiro elemento:")
lista.mostrar()

# e) Pesquisa pelo último caractere do nome
ultimo_caractere = nome[-1]
resultado = lista.pesquisar(ultimo_caractere)

print(
    f"Pesquisa por '{ultimo_caractere}':",
    resultado.valor if resultado else None
)

# f) Exclusão de um elemento que não seja o primeiro
removido = lista.excluir_qualquer("g")
print("Elemento excluído:",
      removido.valor if removido else None)

# g) Verificação da exclusão
resultado = lista.pesquisar("g")
print(
    "Pesquisa por 'g' após a exclusão:",
    resultado.valor if resultado else None
)

print("Lista final:")
lista.mostrar()