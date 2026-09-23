class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostraNo(self):
        print(self.valor, end=" -> ")


class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def inserirInicio(self, valor):
        novo = No(valor)

        novo.proximo = self.primeiro

        self.primeiro = novo

    def mostrar(self):
        if self.primeiro is None:
            print("Lista vazia")
            return None

        atual = self.primeiro

        while atual is not None:
            atual.mostraNo()
            atual = atual.proximo

        print("None")

    def pesquisar(self, valor):
        if self.primeiro is None:
            return None

        atual = self.primeiro

        while atual.valor != valor:
            if atual.proximo is None:
                return None

            atual = atual.proximo

        return atual

    def excluirInicio(self):
        if self.primeiro is None:
            return None

        temp = self.primeiro

        self.primeiro = self.primeiro.proximo

        return temp

    def excluirQualquer(self, valor):
        if self.primeiro is None:
            return None

        atual = self.primeiro
        anterior = self.primeiro

        while atual.valor != valor:
            if atual.proximo is None:
                return None

            anterior = atual
            atual = atual.proximo

        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo

        return atual


lista = ListaEncadeada()

nome = "AUGUSTO"


for caractere in nome:
    lista.inserirInicio(caractere)


print("Lista após as inserções:")
lista.mostrar()


removido = lista.excluirInicio()

print("\nElemento removido do início:", removido.valor)


print("Lista após excluir o primeiro elemento:")
lista.mostrar()



ultimo_caractere = nome[-1]

resultado = lista.pesquisar(ultimo_caractere)

if resultado is None:
    print(
        f"\nCaractere '{ultimo_caractere}' não encontrado."
    )
else:
    print(
        f"\nCaractere '{ultimo_caractere}' encontrado:",
        resultado.valor
    )


valor_excluir = "G"

removido = lista.excluirQualquer(valor_excluir)

if removido is not None:
    print(f"\nElemento removido: {removido.valor}")



resultado = lista.pesquisar(valor_excluir)

if resultado is None:
    print(
        f"Exclusão confirmada: '{valor_excluir}' "
        "não está mais na lista."
    )
else:
    print(
        f"'{valor_excluir}' ainda está na lista."
    )

print("\nLista final:")
lista.mostrar()
